
type payload = Literal of int | Subpackets of packet list
and packet = {version: int; type_id: int; data: payload}

let hex_to_int h =
  let c = int_of_char h in
  if c >= 65 then
    c - 55
  else
    c - 48

let int_to_bin i =
  let rec binify n i acc =
    if n == 0 then acc else
    binify (n - 1) (i lsr 1) ((i land 1)::acc)
  in
  binify 4 i []

let bin_to_int b =
  let rec intify b acc =
    match b with
    | [] -> acc
    | h::t -> intify t ((acc lsl 1) + h)
  in
  intify b 0

let split_n l n =
  let rec s' l n acc =
    if n <= 0 then ((List.rev acc), l) else
    match l with
    | [] -> ([], [])
    | h::t -> s' t (n - 1) (h::acc)
  in
  s' l n []

let pull_int l n =
  let i, rest = split_n l n in
  ((bin_to_int i), rest)

let parse_packet_header pbin =
  let version, p2 = pull_int pbin 3 in
  let type_id, rest = pull_int p2 3 in
  (version, type_id, rest)

let parse_literal pbin =
  let rec pl b acc =
    let chunk, rest = split_n b 5 in
    match chunk with
    | 0::tl -> ((bin_to_int (List.flatten (List.rev (tl::acc)))), rest)
    | 1::tl -> pl rest (tl::acc)
    | _ -> (-1, [])
  in
  pl pbin []

let parse_op_packet_header pbin =
  let len_id, p2 = pull_int pbin 1 in
  let length, rest = pull_int p2 (if len_id == 0 then 15 else 11) in
  (len_id, length, rest)

let rec read_packets_from_bits b =
  let rec read_p b acc =
    if (List.length b) == 0 then List.rev acc else
    let p, rest = parse_packet b in
    read_p rest (p::acc)
  in
  read_p b []

and read_n_packets_from_stream b n =
  let rec read_n b n acc =
    if n <= 0 then ((List.rev acc), b) else
    let packet, rest = parse_packet b in
    read_n rest (n - 1) (packet::acc)
  in
  read_n b n []

and parse_packet_payload len_id length pbin =
  if len_id == 0 then
    let sub_payload, rest = split_n pbin length in
    let sub_packets = read_packets_from_bits sub_payload in
    (sub_packets, rest)
  else
    read_n_packets_from_stream pbin length

and parse_packet pbin =
  let version, type_id, rest = parse_packet_header pbin in
  if type_id == 4 then
    let literal, rest2 = parse_literal rest in
    ({version=version; type_id=type_id; data=Literal literal}, rest2)
  else
    let len_id, length, rest2 = parse_op_packet_header rest in
    let sub_packets, rest3 = parse_packet_payload len_id length rest2 in
    ({version=version; type_id=type_id; data=Subpackets sub_packets}, rest3)

let read_input () =
  let line = read_line () in
  List.init (String.length line) (String.get line)
  |> List.map hex_to_int
  |> List.map int_to_bin
  |> List.flatten

let print_packet p =
  let rec pp indent p =
    Printf.printf "%sVersion: %d Type: %d Data: " (String.make indent ' ') p.version p.type_id;
    match p.data with
    | Literal l -> Printf.printf "%d\n" l
    | Subpackets packets -> (print_endline ""; List.iter (pp (indent + 2)) packets)
  in
  pp 0 p

let[@warning "-partial-match"] get_op_func type_id =
  match type_id with
  | 0 -> List.fold_left (+) 0
  | 1 -> List.fold_left ( * ) 1
  | 2 -> (fun l -> List.fold_left min (List.hd l) l)
  | 3 -> (fun l -> List.fold_left max (List.hd l) l)
  | 5 -> (fun [a;b] -> if a > b then 1 else 0) 
  | 6 -> (fun [a;b] -> if a < b then 1 else 0) 
  | 7 -> (fun [a;b] -> if a == b then 1 else 0) 

let rec eval_packet p =
  match p.data with
  | Literal l -> l
  | Subpackets sub_ps ->
      List.map eval_packet sub_ps
      |> get_op_func p.type_id

let () =
  let input = read_input () in
  let packet, _ = parse_packet input in
  print_packet packet;
  Printf.printf "Ans: %d\n" (eval_packet packet);
  

