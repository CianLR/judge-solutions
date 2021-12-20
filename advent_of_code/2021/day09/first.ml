
let maybe_read_line () =
  try Some(read_line ())
  with End_of_file -> None

let parse_line l =
  List.init (String.length l) (String.get l)
  |> List.map (fun c -> (int_of_char c) - (int_of_char '0'))

let rec read_grid () =
  match maybe_read_line () with
  | None -> []
  | Some(l) -> (parse_line l) :: read_grid ()

let grid_get_val grid (r, c) =
  List.nth (List.nth grid r) c

let adj height width (r, c) =
  [(r + 1, c); (r - 1, c); (r, c + 1); (r, c - 1)]
  |> List.filter (fun (r, c) -> 0 <= r && r < height && 0 <= c && c < width)

let point_is_lowest grid h w p =
  let pval = grid_get_val grid p in
  adj h w p
  |> List.map (grid_get_val grid)
  |> List.for_all ((<) pval)

let find_risk_level grid =
  let h = List.length grid in
  let w = List.length (List.hd grid) in
  List.init h (fun r -> List.init w (fun c -> (r, c)))
  |> List.flatten
  |> List.filter (point_is_lowest grid h w)
  |> List.map (grid_get_val grid)
  |> List.fold_left (fun a x -> a + x + 1) 0

let () =
  let grid = read_grid () in
  let risk_level = find_risk_level grid in
  Printf.printf "Ans: %d\n" risk_level
