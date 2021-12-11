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

let counter l =
  let counter' (z, o) v =
    if v == 0 then (z + 1, o)
    else (z, o + 1)
  in
  List.fold_left counter' (0, 0) l

let bin_to_dec bin =
  let rec btd rbin p acc =
    match rbin with
    | [] -> acc
    | h :: t -> btd t (p * 2) (acc + (h * p))
  in
  btd (List.rev bin) 1 0

let get_col grid ind =
  List.map (fun l -> List.nth l ind) grid

let calc cmp grid =
  let rec calc' grid ind =
    let (z, o) = counter (get_col grid ind) in
    let filter = cmp z o in
    let filtered = List.filter (fun v -> (List.nth v ind) == filter) grid in
    if (List.length filtered) == 1 then List.hd filtered
    else calc' filtered (ind + 1)
  in
  calc' grid 0

let oxygen = calc (fun z o -> if z > o then 0 else 1)
let co2 = calc (fun z o -> if o < z then 1 else 0)

let () =
  let (grid, height, width) = convert_to_grid (read_input ()) in
  let oxy = oxygen grid in
  let carbon = co2 grid in
  Printf.printf "Ans: %d\n" ((bin_to_dec oxy) * (bin_to_dec carbon))
