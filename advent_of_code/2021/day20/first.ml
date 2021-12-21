
let maybe_read_line () =
  try Some(read_line ())
  with End_of_file -> None

let rec read_grid () =
  match maybe_read_line () with
  | Some l -> l :: read_grid ()
  | None -> []

let read_input () =
  let algo = read_line () in
  let _ = read_line () in
  let image = read_grid () in
  (algo, image)

let adj (r, c) =
  [
    (r - 1, c - 1); (r - 1, c); (r - 1, c + 1);
    (r, c - 1);     (r, c);     (r, c + 1);
    (r + 1, c - 1); (r + 1, c); (r + 1, c + 1)
  ]

let grid_to_set grid =
  let set = Hashtbl.create 100 in
  let add_point = Hashtbl.replace set in
  List.iteri (fun r row -> String.iteri (fun c v -> add_point (r, c) (v == '#')) row) grid;
  set

let hash_get_default h k d =
  match Hashtbl.find_opt h k with
  | None -> d
  | Some v -> v

let get_value image default p =
  adj p
  |> List.map (fun p -> if hash_get_default image p default then 1 else 0)
  |> List.fold_left (fun a v -> (a lsl 1) + v) 0

let get_image_bounds image =
  let maybe_compare cmp getter v _ a =
    match a with
    | None -> Some (getter v)
    | Some x -> Some (cmp x (getter v))
  in
  let get_r (r, _) = r in
  let get_c (_, c) = c in
  let min_r = Hashtbl.fold (maybe_compare min get_r) image None in
  let max_r = Hashtbl.fold (maybe_compare max get_r) image None in
  let min_c = Hashtbl.fold (maybe_compare min get_c) image None in
  let max_c = Hashtbl.fold (maybe_compare max get_c) image None in
  (
    (Option.get min_r) - 2,
    (Option.get max_r) + 2,
    (Option.get min_c) - 2,
    (Option.get max_c) + 2
  )

let algo_result algo image default p =
  let v = get_value image default p in
  (String.get algo v) == '#'

let apply_algo algo default image =
  let min_r, max_r, min_c, max_c = get_image_bounds image in
  let new_image = Hashtbl.create (Hashtbl.length image) in
  for r = min_r to max_r do
    for c = min_c to max_c do
      Hashtbl.replace new_image (r, c) (algo_result algo image default (r, c))
    done
  done;
  new_image

let print_image image =
  let min_r, max_r, min_c, max_c = get_image_bounds image in
  for r = min_r to max_r do
    for c = min_c to max_c do
      Printf.printf (if Hashtbl.mem image (r, c) then "#" else ".")
    done;
    print_endline ""
  done

let count_on image =
  Hashtbl.fold (fun k v a -> if v then a + 1 else a) image 0

let () =
  let algo, image_grid = read_input () in
  let image = grid_to_set image_grid in
  let i2 = apply_algo algo false image in
  let i3 = apply_algo algo true i2 in
  Printf.printf "Ans: %d\n" (count_on i3)
