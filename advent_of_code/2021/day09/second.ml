
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

let bfs grid h w p =
  let seen = Hashtbl.create (h * w) in
  let rec bfs' u =
    Hashtbl.replace seen u true;
    adj h w u
    |> List.filter (fun p -> (grid_get_val grid p) != 9)
    |> List.filter (fun p -> not (Hashtbl.mem seen p))
    |> List.iter bfs'
  in
  bfs' p;
  Hashtbl.length seen

let find_risk_level grid =
  let h = List.length grid in
  let w = List.length (List.hd grid) in
  let basins = List.init h (fun r -> List.init w (fun c -> (r, c)))
    |> List.flatten
    |> List.filter (point_is_lowest grid h w)
    |> List.map (bfs grid h w)
    |> List.sort compare
    |> List.rev
  in
  match basins with
  | a::b::c::_ -> a * b * c
  | _ -> 0


let () =
  let grid = read_grid () in
  let risk_level = find_risk_level grid in
  Printf.printf "Ans: %d\n" risk_level
