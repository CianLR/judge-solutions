open List
open String
open Str

let matches_color str =
        let pink_re = Str.regexp_string "pink" in
        let rose_re = Str.regexp_string "rose" in
        let low_str = String.lowercase_ascii str in
        try ignore (Str.search_forward pink_re low_str 0); true
        with Not_found ->
                try ignore (Str.search_forward rose_re low_str 0); true
                with Not_found -> false

let rec read_n_lines n =
        match n with
        | 0 -> []
        | _ -> read_line () :: read_n_lines (n - 1)

let () =
        let n = read_int () in
        let colors = read_n_lines n in
        let matches = List.length (List.filter matches_color colors) in
        match matches with
        | 0 -> print_endline "I must watch Star Wars with my daughter"
        | _ -> print_int matches; print_endline ""

