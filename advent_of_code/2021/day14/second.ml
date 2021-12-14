
let maybe_read_line () =
  try Some(read_line ())
  with End_of_file -> None

let explode s =
  List.rev (String.fold_left (fun a c -> c::a) [] s)

let read_input () =
  let start = explode (read_line ()) in
  let _ = read_line () in
  let rec r () =
    match maybe_read_line () with
    | Some(l) -> l::(r ())
    | None -> []
  in
  (start, r ())

let parse_rule line =
  Scanf.sscanf line "%c%c -> %c" (fun a b x -> (a, b, x))

let build_rule_map rules =
  let rmap = Hashtbl.create (List.length rules) in
  List.iter (fun (a, b, x) -> Hashtbl.replace rmap (a, b) x) rules;
  rmap

let hash_inc hash k v =
  let c =
    match Hashtbl.find_opt hash k with
    | Some(x) -> x
    | None -> 0
  in
  Hashtbl.replace hash k (c + v)

let create_pairs l =
  let p = Hashtbl.create (List.length l) in
  let rec add l =
    match l with
    | [] | _::[] -> p
    | a::b::tl -> begin hash_inc p (a, b) 1; add (b::tl) end
  in
  add l

let apply_rules pairs rules =
  let h = Hashtbl.create (Hashtbl.length pairs) in
  let iter k v =
    match Hashtbl.find_opt rules k with
    | None -> hash_inc h k v
    | Some(c) ->
        let a, b = k in begin
        hash_inc h (a, c) v;
        hash_inc h (c, b) v
        end
  in
  Hashtbl.iter iter pairs;
  h

let rec apply_n pairs rules n =
  if n <= 0 then pairs else apply_n (apply_rules pairs rules) rules (n - 1)

let get_freq pairs s =
  let f = Hashtbl.create 10 in
  let count (_, b) v =
    hash_inc f b v
  in
  Hashtbl.iter count pairs;
  hash_inc f s 1;
  f

let most_least_freq p s =
  let freq = get_freq p s in
  let most = Hashtbl.fold (fun _ v a -> if a > v then a else v) freq 0 in
  let least = Hashtbl.fold (fun _ v a -> if a < v then a else v) freq most in
  (most, least)

let () =
  let start, lines = read_input () in
  let rules = build_rule_map (List.map parse_rule lines) in
  let spairs = create_pairs start in
  let final = apply_n spairs rules 40 in
  let most, least = most_least_freq final (List.hd start) in
  Printf.printf "Ans: %d\n" (most - least)

