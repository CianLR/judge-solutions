
let kPrime = 1000000007

let read_list () =
  read_line ()
  |> String.split_on_char ' '
  |> List.map int_of_string

let combinations songs =
  let rec comb' threes twos ones = function
    | [] -> ones
    | h :: t ->
      if h = 3 then
        comb' (threes + 1) twos ones t
      else if h == 2 then
        comb' threes (((2 * twos) + threes) mod kPrime) ones t
      else
        comb' threes twos ((ones + twos) mod kPrime) t
  in
  comb' 0 0 0 (List.rev songs)

let () =
  let _ = read_int () in
  let songs = read_list () in
  let cmb = combinations songs in
  Printf.printf "%d\n" cmb

