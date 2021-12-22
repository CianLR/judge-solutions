
type tree = Leaf of int | Node of tree * tree

let maybe_read_line () =
  try Some (read_line ())
  with End_of_file -> None

let rec read_input () =
  match maybe_read_line () with
  | Some l -> l :: read_input ()
  | None -> []

let char_to_int c =
  (int_of_char c) - (int_of_char '0')

let tree_parse s =
  let rec tp s i =
    if String.get s i == '[' then
      let left, i2 = tp s (i + 1) in
      (* i2 == ',' *)
      let right, i3 = tp s (i2 + 1) in
      (* i3 == ']' *)
      ((Node (left, right)), (i3 + 1))
    else
      ((Leaf (char_to_int (String.get s i))), (i + 1))
  in
  let t, _ = tp s 0 in
  t

let tree_add a b =
  Node (a, b)

let rec tree_to_string p =
  match p with
  | Leaf i -> Printf.sprintf "%d" i
  | Node (a, b) -> Printf.sprintf "[%s,%s]" (tree_to_string a) (tree_to_string b)

let tree_explode p =
  let rec add_right p x =
    if x == 0 then p else
    match p with
    | Leaf i -> Leaf (i + x)
    | Node (l, r) -> Node (l, (add_right r x))
  in
  let rec add_left p x =
    if x == 0 then p else
    match p with
    | Leaf i -> Leaf (i + x)
    | Node (l, r) -> Node ((add_left l x), r)
  in
  let rec texpl p depth =
    if depth == 4 then match p with
      | Node (Leaf lx, Leaf rx) -> (Leaf 0, Some (lx, rx))
      | _ -> (p, None)
    else match p with
      | Leaf i -> (Leaf i, None)
      | Node (l, r) ->
          let nl, res = texpl l (depth + 1) in
          match res with
          | Some (lx, rx) -> (Node (nl, (add_left r rx)), Some (lx, 0))
          | None ->
            let nr, res2 = texpl r (depth + 1) in
            match res2 with
            | None -> (Node (nl, nr), None)
            | Some (lx, rx) -> (Node ((add_right nl lx), nr), Some (0, rx))
  in
  texpl p 0

let rec tree_split p =
  let split i =
    Node (Leaf (i / 2), Leaf ((i / 2) + (i mod 2)))
  in
  match p with
  | Leaf i -> if i > 9 then (split i, true) else (Leaf i, false)
  | Node (l, r) ->
      let nl, change = tree_split l in
      if change then (Node (nl, r), true) else
      let nr, change2 = tree_split r in
      (Node (l, nr), change2)

let rec tree_eq a b =
  match (a, b) with
  | (Leaf x, Leaf y) -> x == y
  | (Node (a1, a2), Node (b1, b2)) -> (tree_eq a1 b1) && (tree_eq a2 b2)
  | _ -> false

let rec resolve p =
  let new_p, change = tree_explode p in
  if Option.is_some change then begin
    resolve new_p
  end else begin
  assert (tree_eq p new_p);
  let new_p2, change = tree_split p in
  if change then begin
    resolve new_p2
  end else begin
    assert (tree_eq p new_p2);
    p
  end end

let rec tree_magnitude p =
  match p with
  | Leaf i -> i
  | Node (l, r) -> (3 * (tree_magnitude l)) + (2 * (tree_magnitude r))

let rec tree_print p =
  print_endline (tree_to_string p)

let combine a b =
  resolve (tree_add a b)

let mag_combine a b =
  tree_magnitude (combine a b)

let all_pairs l =
  let p = ref [] in
  for i = 0 to (l - 2) do
    for j = (i + 1) to (l - 1) do
      p := (i, j)::!p
    done
  done;
  !p

let max_magnitude trees =
  all_pairs (List.length trees)
  |> List.map (fun (i, j) -> ((List.nth trees i), (List.nth trees j)))
  |> List.map (fun (a, b) -> max (mag_combine a b) (mag_combine b a))
  |> List.fold_left max 0

let () =
  let input = read_input () in
  let trees = List.map tree_parse input in
  Printf.printf "Magnitude: %d\n" (max_magnitude trees)

