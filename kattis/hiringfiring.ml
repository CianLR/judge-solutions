
let read_days n =
  let read_day _ =
    let [fire; hire] = String.split_on_char ' ' (read_line ()) in
    (int_of_string fire, int_of_string hire)
  in
  List.init n read_day

let pop_n_jobs s n =
  let rec pop' s n acctbl =
    if n = 0 then acctbl else
    let jobs, worker = Stack.pop s in
    Hashtbl.replace acctbl worker true;
    if n >= jobs then
      pop' s (n - jobs) acctbl
    else begin
      Stack.push (jobs - n, worker) s;
      acctbl
    end
  in
  let wtbl = Hashtbl.create 1024 in
  pop' s n wtbl

let get_first_not_in t =
  let rec gfni t i =
    if Hashtbl.mem t i then
      gfni t (i + 1)
    else
      i
  in
  gfni t 1

let get_workers days =
  let rec get_workers' s acc = function
    | [] -> List.rev acc
    | h :: t ->
        let fire, hire = h in
        let workers = pop_n_jobs s fire in
        let next_worker = get_first_not_in workers in begin
        if hire != 0 then Stack.push (hire, next_worker) s;
        get_workers' s (next_worker :: acc) t
        end
  in
  let s = Stack.create () in
  get_workers' s [] days

let () =
  let n = read_int () in
  let days = read_days n in
  let workers = get_workers days in
  let num_workers = List.fold_left max 0 workers in
  print_int num_workers;
  print_newline ();
  for i = 0 to (List.length workers) - 1 do
    Printf.printf "%d " (List.nth workers i)
  done;
  print_newline ();

