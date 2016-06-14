(defn digits-and-bases [n base]
  {:pre [(>= n 0)]}
  (letfn [(step [r n base]
            (if (zero? n)
              r
              (step (conj r (mod n base))
                    (quot n base)
                    base)))]
    (if (zero? n)
      '(0)
      (step '() n base))))
