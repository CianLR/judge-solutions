open String
open List
open Str
open Fun

let get_input () =
  List.init 5 (fun _ -> read_line ())

let match_name name =
  let re = Str.regexp ".*FBI.*" in
  Str.string_match re name 0

let index_if_match index elm =
  if match_name elm then Some(index + 1) else None

let () =
  let blimps = get_input () in
  let matches = List.mapi index_if_match blimps
                |> List.filter_map Fun.id in
  match matches with
  | [] -> print_endline "HE GOT AWAY!"
  | _ -> print_endline (String.concat " " (List.map string_of_int matches))

