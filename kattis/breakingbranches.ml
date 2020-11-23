
let () =
  let n = read_int () in
  if n mod 2 = 0 then
    print_endline "Alice\n1"
  else
    print_endline "Bob"
