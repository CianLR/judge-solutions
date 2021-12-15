
let read_state () =
  read_line ()
  |> String.split_on_char ','
  |> List.map int_of_string

let hash_inc h k x =
  let curr =
    match Hashtbl.find_opt h k with
    | Some(c) -> c
    | None -> 0
  in
  Hashtbl.replace h k (curr + x)

let create_state_map state =
  let map = Hashtbl.create 10 in
  List.iter (fun n -> hash_inc map n 1) state;
  map

let apply_day state =
  let nstate = Hashtbl.create (Hashtbl.length state) in
  Hashtbl.iter (fun k v ->
    if k > 0 then hash_inc nstate (k - 1) v
    else begin
      hash_inc nstate 6 v;
      hash_inc nstate 8 v
    end) state;
  nstate

let rec apply_n_days n state =
  if n <= 0 then state else apply_n_days (n - 1) (apply_day state)

let count_fish state =
  Hashtbl.fold (fun _ v a -> v + a) state 0

let () =
  let inital_state = read_state () in
  let state_map = create_state_map inital_state in
  let nstate = apply_n_days 80 state_map in
  Printf.printf "Ans: %d\n" (count_fish nstate);


