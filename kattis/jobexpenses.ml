open String
open List
open Format

let read_int () =
        int_of_string (read_line ())

let read_int_list () =
        read_line()
        |> String.split_on_char ' '
        |> List.map int_of_string

let rec sum_neg acc nums =
        match nums with
        | [] -> acc
        | head :: tail ->
            match head with
            | _ when head < 0 -> sum_neg (acc - head) tail
            | _ -> sum_neg acc tail


let () =
        let n = read_int () in
        printf "%d\n" (
        match n with
        | 0 -> 0
        | _ -> read_int_list () |> sum_neg 0)

