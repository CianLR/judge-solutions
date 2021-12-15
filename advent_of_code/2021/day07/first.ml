
let read_crabs () =
  read_line ()
  |> String.split_on_char ','
  |> List.map int_of_string

let sum =
  List.fold_left (+) 0

let evaluate_pos crabs p =
  List.map (fun c -> abs (p - c)) crabs
  |> sum

let find_best_pos crabs =
  let max_crab = List.fold_left max 0 crabs in
  let min_crab = List.fold_left min max_crab crabs in
  List.init (max_crab - min_crab) (fun k -> (evaluate_pos crabs (min_crab + k)))
  |> List.fold_left min (max_crab * List.length crabs)

let () =
  let crabs = read_crabs () in
  let best_pos = find_best_pos crabs in
  Printf.printf "Ans: %d\n" best_pos

