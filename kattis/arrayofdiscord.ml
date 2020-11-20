open String
open List

let read_int () =
  read_line ()
  |> String.trim
  |> int_of_string

let read_int_list () =
  read_line ()
  |> String.split_on_char ' '
  |> List.map int_of_string

let print_list l =
  List.map string_of_int l
  |> String.concat " "
  |> print_endline

let highest n =
  let rec highest' s =
    match s () with
    | Seq.Nil -> fun () -> Seq.Nil
    | Cons (c, tail) ->
        if c != '9' then
          fun () -> Cons ('9', tail)
        else
          fun () -> Cons (c, highest' tail)
  in
  string_of_int n
  |> String.to_seq
  |> highest'
  |> String.of_seq
  |> int_of_string

let lowest n =
  let nstring = string_of_int n in
  if String.length nstring = 1 then
    0
  else if nstring.[0] != '1' then
    nstring
    |> String.mapi (fun i c -> if i = 0 then '1' else c)
    |> int_of_string
  else
  let rec lowest' s =
    match s () with
    | Seq.Nil -> fun () -> Seq.Nil
    | Cons (c, tail) ->
        if c != '0' then
          fun () -> Cons ('0', tail)
        else
          fun () -> Cons (c, lowest' tail)
  in
  String.sub nstring 1 (String.length nstring - 1)
  |> String.to_seq
  |> lowest'
  |> String.of_seq
  |> (^) "1"
  |> int_of_string

let rec get_highest = function
  | [] -> []
  | [x] -> [x]
  | l :: r :: t ->
      let hl = highest l in
      if hl > r then
        hl :: r :: t
      else
        l :: get_highest (r :: t)

let rec get_lowest = function
  | [] -> []
  | [x] -> [x]
  | l :: r :: t ->
      let lr = lowest r in
      if l > lr then
        l :: lr :: t
      else
        l :: get_lowest (r :: t)

let rec is_sorted = function
  | [] | [_] -> true
  | l :: r :: t ->
      l <= r && is_sorted (r :: t)

let () =
  let _ = read_int () in
  let l = read_int_list () in
  let highest = get_highest l in
  let lowest = get_lowest l in
  if not (is_sorted highest) then
    print_list highest
  else if not (is_sorted lowest) then
    print_list lowest
  else
    print_endline "impossible"

