open String
open List

let maybe_read_line () =
        try Some(read_line ())
        with End_of_file -> None ;;

let print_int n =
        print_endline (string_of_int n) ;;

let rec outlet_count outlets =
        match outlets with
        | [] -> 1
        | head :: tail -> (head - 1) + (outlet_count tail) ;;

let get_outlet_list str =
        match String.split_on_char ' ' str with
        | head :: tail -> List.map int_of_string tail
        | [] -> [] ;;

let run_single_case () =
        match maybe_read_line () with
        | None -> ()
        | Some(line) -> print_int (outlet_count (get_outlet_list line)) ;;

let rec run_test_cases n =
        match n with
        | 0 -> ()
        | _ -> let _ = run_single_case () in
               run_test_cases (n - 1) ;;

let () =
        match maybe_read_line () with
        | None -> ()
        | Some(line) -> run_test_cases (int_of_string line) ;;
       
