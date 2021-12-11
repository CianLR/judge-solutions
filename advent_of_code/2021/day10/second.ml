
let explode s = List.init (String.length s) (String.get s)

let points c =
  match c with
  | ')' -> 1
  | ']' -> 2
  | '}' -> 3
  | '>' -> 4
  | _ -> 0
    
let matching_bracket b =
  match b with
  | '{' -> Some('}')
  | '(' -> Some(')')
  | '[' -> Some(']')
  | '<' -> Some('>')
  | _ -> None
    
let completion s =
  let rec completion' s q =
    match s with
    | [] -> Some(q)
    | c :: t ->
        match matching_bracket c with
        | Some(close) -> completion' t (close :: q)
        | None ->
            match q with
            | qh :: qt -> if c != qh then None else completion' t qt 
            | [] -> None
  in
  completion' (explode s) []
            
let maybe_read_line () =
  try Some(read_line ())
  with End_of_file -> None

let rec read_input () =
  match maybe_read_line () with
  | Some(l) -> l :: read_input ()
  | None -> [] 
            
let score_ending score c =
  (score * 5) + points c

let () =
  let inputs = read_input () in
  let endings = List.filter_map completion inputs in
  let scores = List.map (List.fold_left score_ending 0) endings in
  let sorted_scores = List.fast_sort compare scores in
  let mid = List.nth sorted_scores ((List.length sorted_scores) / 2) in
  Printf.printf "Score: %d\n" mid

