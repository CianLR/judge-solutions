module Point =
  struct
    type t = int * int
    let compare (r1, c1) (r2, c2) =
      let comp1 = compare r1 r2 in
      if comp1 != 0 then comp1
      else compare c1 c2
    let to_string (r, c) =
      Printf.sprintf "(%d, %d)" r c
  end

module CostPoint =
  struct
    type t = int * Point.t
    let compare (c1, p1) (c2, p2) =
      let c = compare c1 c2 in
      if c != 0 then c else Point.compare p1 p2
  end

module StateSet = Set.Make(CostPoint)
module SeenSet = Set.Make(Point)

let explode line =
  List.init (String.length line) (String.get line)

let char_to_digit c =
  (int_of_char c) - (int_of_char '0')

let maybe_read_line () =
  try Some(read_line ())
  with End_of_file -> None

let rec read_input () =
  match maybe_read_line () with
  | Some(l) -> (List.map char_to_digit (explode l)) :: read_input ()
  | None -> []

let adj height width (r, c) =
  [(r + 1, c); (r - 1, c); (r, c + 1); (r, c - 1)]
  |> List.filter (fun (r, c) -> 0 <= r && r < height && 0 <= c && c < width)

let get_value grid (r, c) =
  List.nth (List.nth grid r) c

let print_q q =
  Printf.printf "PQ:\n";
  List.iter (fun (k, (r, c)) -> Printf.printf "  (%d (%d %d))\n" k r c) (StateSet.elements q)

let dijkstra grid height width s e =
  let q = ref (StateSet.add (0, s) StateSet.empty) in
  let seen = ref SeenSet.empty in
  let final = ref (-1) in
  while not (StateSet.is_empty !q) && !final == -1 do
    let c, u = StateSet.min_elt !q in
    q := StateSet.remove (c, u) !q;
    if SeenSet.mem u !seen then () else begin
    seen := SeenSet.add u !seen;
    if 0 == Point.compare u e then final := c else begin
    adj height width u
    |> List.filter (fun v -> not (SeenSet.mem v !seen))
    |> List.iter (fun v ->
        let new_cost = c + (get_value grid v) in
        q := StateSet.add (new_cost, v) !q
    ) end end
  done;
  !final

let () =
  let grid = read_input () in
  let height = List.length grid in
  let width = List.length (List.hd grid) in
  let cost = dijkstra grid height width (0, 0) (height - 1, width - 1) in
  Printf.printf "Cost: %d\n" cost

