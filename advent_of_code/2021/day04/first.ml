
let read_calls () =
  let s = read_line () in
  List.map int_of_string (String.split_on_char ',' s)

let parse_line s =
  let split = String.split_on_char ' ' s in
  let fsplit = List.filter (fun s -> (String.length s) > 0) split in
  List.map int_of_string fsplit

let read_board () =
  let _ = read_line () in
  let raw_lines = List.init 5 (fun _ -> read_line ()) in
  List.map parse_line raw_lines

let maybe_read_board () =
  try Some(read_board ()) 
  with End_of_file -> None

let rec read_boards () =
  match maybe_read_board () with
  | None -> []
  | Some(b) -> b :: read_boards ()

let mark_board num =
  List.map (List.map (fun v -> if v == num then -1 else v))

let print_board =
  List.iter (fun row -> List.iter (Printf.printf "%d ") row; Printf.printf "\n")

let transpose grid width =
  List.init width (fun w -> List.map (fun l -> List.nth l w) grid)

let is_winner board =
  let all_marked = List.for_all ((==) (-1)) in
  if List.exists all_marked board then true else
  let board' = transpose board 5 in
  List.exists all_marked board' 

let sum_board =
  List.fold_left (fun acc -> List.fold_left (fun a x -> if x == -1 then a else a + x) acc) 0

let rec run_game calls boards =
  match calls with
  | [] -> 0
  | call :: tail ->
      let new_boards = List.map (mark_board call) boards in
      let winners = List.filter is_winner new_boards in
      if List.length winners == 0 then
        run_game tail new_boards
      else
        call * (sum_board (List.hd winners))

let () =
  let calls = read_calls () in
  let boards = read_boards () in
  let score = run_game calls boards in
  Printf.printf "Score: %d\n" score
