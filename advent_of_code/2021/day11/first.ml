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
  let grid = Hashtbl.create (height * width) in
  List.iteri (fun h l -> List.iteri (fun w v -> Hashtbl.replace grid (h, w) v) l) intgrid;
  (grid, height, width)

let print_grid grid height width =
  for h = 0 to height - 1 do
    for w = 0 to width - 1 do
      Printf.printf "%d" (Hashtbl.find grid (h, w))
    done;
    Printf.printf "\n"
  done

let get_neighbours height width (h, w) =
  let valid height width (h, w) =
    0 <= h && h < height && 0 <= w && w < width
  in
  let neighbours = [
    (h + 1, w); (h + 1, w + 1); (h, w + 1); (h - 1, w + 1);
    (h - 1, w); (h - 1, w - 1); (h, w - 1); (h + 1, w - 1)
  ] in
  List.filter (valid height width) neighbours

let hash_increment table key =
  Hashtbl.replace table key ((Hashtbl.find table key) + 1)

let rec visit grid height width =
  let rec visit' grid height width flashes q =
    match q with
    | [] -> flashes
    | cords :: tl ->
      if Hashtbl.find grid cords <= 9 then
        visit' grid height width flashes tl
      else
        let neighbours = get_neighbours height width cords in
        List.iter (hash_increment grid) neighbours;
        Hashtbl.replace grid cords 0;
        visit' grid height width (cords :: flashes) (tl @ neighbours)
  in
  let all_cells = List.flatten (List.init height (fun h -> List.init width (fun w -> (h, w)))) in
  visit' grid height width [] all_cells

let run_step grid height width =
  Hashtbl.filter_map_inplace (fun _ v -> Some(v + 1)) grid;
  let flashes = visit grid height width in
  List.iter (fun cords -> Hashtbl.replace grid cords 0) flashes;
  List.length flashes

let () =
  let input = read_input () in
  let (grid, height, width) = convert_to_grid input in
  let flashes = List.init 100 (fun _ -> run_step grid height width) in
  Printf.printf "%d\n" (List.fold_left (fun a x -> a + x) 0 flashes);
  print_grid grid height width

