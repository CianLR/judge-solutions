
let read_stacks () =
  read_line ()
  |> String.split_on_char ' '
  |> List.map int_of_string

let get_largest not_i l =
  let get_largest' (not_i, i, large, large_i) x =
        if x > large && i != not_i then
          (not_i, (i + 1), x, i)
        else
          (not_i, (i + 1), large, large_i)
  in
  let _, _, _, li = List.fold_left get_largest' (not_i, 0, -1, -1) l in
  li

let largest2 lst =
  let lrg1 = get_largest (-1) lst in
  let lrg2 = get_largest lrg1 lst in
  lrg1, lrg2

let decrement i l =
  let rec decrement' ci di acc = function
    | [] -> acc
    | h :: t ->
        if ci == di then
          (List.rev ((h - 1) :: acc)) @ t
        else
          decrement' (ci + 1) di (h :: acc) t
  in
  decrement' 0 i [] l

let rec is_winable stacks =
  let rec is_winable' acc stacks =
    let l1, l2 = largest2 stacks in
    let s1 = List.nth stacks l1 in
    let s2 = List.nth stacks l2 in
    if s1 == 0 && s2 == 0 then
      Some acc
    else if s1 == 0 || s2 == 0 then
      None
    else
      stacks
      |> decrement l1
      |> decrement l2
      |> is_winable' ((l1, l2) :: acc)
    in
    is_winable' [] stacks

let rec print_list = function
  | [] -> ()
  | h :: t ->
      let a, b = h in
      Printf.printf "%d %d\n" (a + 1) (b + 1);
      print_list t

let () =
  let _ = read_int () in
  let stacks = read_stacks () in
  match is_winable stacks with
  | None -> print_endline "no"
  | Some moves ->
      print_endline "yes";
      print_list moves

