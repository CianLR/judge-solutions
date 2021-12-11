let explode s = List.init (String.length s) (String.get s)

let maybe_read_line () =
  try Some(read_line ())
  with End_of_file -> None

let rec read_input () =
  match maybe_read_line () with
  | Some(l) -> l :: read_input ()
  | None -> []

let char_to_int c =
  (int_of_char c) - (int_of_char '0')

let convert_to_grid input =
  let exploded = List.map explode input in
  let intgrid = List.map (List.map char_to_int) exploded in
  let height = List.length intgrid in
  let width = List.length (List.nth intgrid 0) in
  (intgrid, height, width)

let transpose grid width =
  List.init width (fun w -> List.map (fun l -> List.nth l w) grid)

let most_common l =
  let rec mc l z o =
    match l with
    | [] -> if z > o then 0 else 1
    | h :: t ->
        if h == 0 then mc t (z + 1) o
        else mc t z (o + 1)
  in
  mc l 0 0

let rec swap l =
  match l with
  | [] -> []
  | h :: t -> (if h == 0 then 1 else 0) :: swap t

let bin_to_dec bin =
  let rec btd rbin p acc =
    match rbin with
    | [] -> acc
    | h :: t -> btd t (p * 2) (acc + (h * p))
  in
  btd (List.rev bin) 1 0

let () =
  let (grid, height, width) = convert_to_grid (read_input ()) in
  let tgrid = transpose grid width in
  let eps = List.map most_common tgrid in
  let gam = swap eps in
  Printf.printf "Ans: %d\n" ((bin_to_dec eps) * (bin_to_dec gam))
