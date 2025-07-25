!determine_coverage.

+!determine_coverage : req(REQ) & spec(S) <-
    .examine(S, REQ, RES);
    +covered(RES).

+!determine_coverage <- !determine_coverage.

+covered(true) <- .print("The coverage is OK").

+covered(false) <- .print("The coverage is incomplete") ; !ask_for_completion.

+!ask_for_completion <- +completeme.