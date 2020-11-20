open String
open Str

let get_names () =
  read_line ()
  |> String.trim
  |> String.split_on_char ' '

let trim_name n =
  let re = Str.regexp {|^\(.*\)\([aeiou]\|ex\)$|} in
  let m = Str.string_match re n 0 in
  if not m then n else
  Str.matched_group 1 n

let () =
  let [y; p] = get_names () in
  let e = trim_name y in
  print_endline (e ^ "ex" ^ p)

