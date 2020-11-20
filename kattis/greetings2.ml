open String
open Seq
open List

let () =
  let greet = read_line () in
  let e_count =
    greet
    |> String.to_seq
    |> Seq.fold_left (fun a c -> if c == 'e' then a + 1 else a) 0
  in
  let e_out = List.init (e_count * 2) (fun _ -> 'e') in
  let out = "h" ^ (List.to_seq e_out |> String.of_seq) ^ "y" in
  print_endline out

