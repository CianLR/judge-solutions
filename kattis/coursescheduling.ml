open List

let parse_reg r =
  match String.split_on_char ' ' r with
  | [first; sur; cls] -> (first ^ " " ^ sur, cls)
  | _ -> ("", "")

let get_or_create h cls =
  match Hashtbl.find_opt h cls with
  | Some t -> t
  | None ->
      Hashtbl.add h cls (Hashtbl.create (1 lsl 10));
      Hashtbl.find h cls

let count_registrations reg =
  let class_map = Hashtbl.create (1 lsl 10) in
  let rec count' = function
    | [] -> class_map
    | h :: t ->
        let name, cls = parse_reg h in
        let cls_tbl = get_or_create class_map cls in
        Hashtbl.replace cls_tbl name true;
        count' t
  in
  count' reg

let print_registrations class_map =
  let fold_class_counts cls smap l =
    let s = Printf.sprintf "%s %d" cls (Hashtbl.length smap) in
    s :: l
  in
  Hashtbl.fold fold_class_counts class_map []
  |> List.sort String.compare
  |> List.iter print_endline

let () =
  let n = read_int () in
  let registrations = List.init n (fun _ -> read_line ()) in
  count_registrations registrations
  |> print_registrations

