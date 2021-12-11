
let explode s = List.init (String.length s) (String.get s)

let points c =
  match c with
  | ')' -> 3
  | ']' -> 57
  | '}' -> 1197
  | '>' -> 25137
  | _ -> 0
    
let matching_bracket b =
  match b with
  | '{' -> Some('}')
  | '(' -> Some(')')
  | '[' -> Some(']')
  | '<' -> Some('>')
  | _ -> None
    
let first_illegal s =
  let rec first_illegal' s q =
    match s with
    | [] -> None
    | c :: t ->
        match matching_bracket c with
        | Some(close) -> first_illegal' t (close :: q)
        | None ->
            match q with
            | qh :: qt -> if c != qh then Some(c) else first_illegal' t qt 
            | [] -> Some(c)
  in
  first_illegal' (explode s) []
            
let maybe_read_line () =
  try Some(read_line ())
  with End_of_file -> None

let rec read_input () =
  match maybe_read_line () with
  | Some(l) -> l :: read_input ()
  | None -> [] 
            

let () =
  let inputs = read_input () in
  let illegals = List.filter_map first_illegal inputs in
  let all_points = List.map points illegals in
  let score = List.fold_left (fun x y -> x + y) 0 all_points in
  Printf.printf "Score %d\n" score

