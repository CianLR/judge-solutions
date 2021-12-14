
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

let apply_rules rules tmpl =
  let rec apply tmpl acc =
    match tmpl with
    | [] -> []
    | a::[] -> List.rev (a::acc)
    | a::b::tl ->
        match Hashtbl.find_opt rules (a, b) with
        | None -> apply (b::tl) (a::acc)
        | Some(x) -> apply (b::tl) (x::a::acc)
  in
  apply tmpl []

let rec apply_n rules tmpl n =
  if n <= 0 then tmpl else apply_n rules (apply_rules rules tmpl) (n - 1)

let get_freq l =
  let freq = Hashtbl.create 10 in
  let count v =
    let c =
      match Hashtbl.find_opt freq v with
      | Some(x) -> x
      | None -> 0
    in
    Hashtbl.replace freq v (c + 1)
  in
  List.iter count l;
  freq

let most_least_freq l =
  let freq = get_freq l in
  let most = Hashtbl.fold (fun _ v a -> if a > v then a else v) freq 0 in
  let least = Hashtbl.fold (fun _ v a -> if a < v then a else v) freq most in
  (most, least)

let () =
  let start, lines = read_input () in
  let rules = build_rule_map (List.map parse_rule lines) in
  let final = apply_n rules start 10 in
  let most, least = most_least_freq final in
  Printf.printf "Ans: %d\n" (most - least)

