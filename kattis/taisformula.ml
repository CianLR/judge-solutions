open String
open List

type sample = Sample of int * float

let sample_from_string str =
  match String.split_on_char ' ' str with
  | [t; v] -> Sample (int_of_string t, float_of_string v)
  | _ -> Sample (-1, -1.)

let get_samples n =
  let sample_strs = List.init n (fun _ -> read_line ()) in
  List.map sample_from_string sample_strs

let calc_trapezoid s1 s2 =
  let Sample (t1, v1) = s1 in
  let Sample (t2, v2) = s2 in
  ((v1 +. v2) /. 2000.0) *. float_of_int (t2 - t1)

let () =
  let readings = read_int () in
  let samples = get_samples readings in
  let rec loop smpls acc =
    match smpls with
    | a :: b :: rest -> loop (b :: rest) (acc +. calc_trapezoid a b)
    | _ -> acc in
  print_float (loop samples 0.0);
  print_newline ()

