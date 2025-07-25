!start.

+!start <-
    +car(red).

+spec(C) <- .print("Spec set").

+req(R) <- !determine_coverage.

+!determine_coverage : req(REQ) & spec(S) <-
    .examine(S, REQ, RES);
    +covered(RES).
