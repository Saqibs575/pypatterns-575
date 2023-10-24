from datetime import sleep
class Name :
    def get_name(self, name, symbol=None, animate=False) :
        if animate :
            time = 0.02
        else :
            time = 0
        alphabets = self.__all_alphabets()
        try :
            if not symbol :
                symbol = "*"
            lst = [alphabets[letter] for letter in name.upper()]
            for i in range(9) :
                for j in range(len(name)) :
                    print(lst[j][i].replace("*", symbol), end="")
                    sleep(time)
                sleep(time)
                print()
        except Exception as e:
            raise ValueError("Only alphabets and spaces are allowed")

    def __all_alphabets(self) :
    # ALL ALPHABETS        
        A = [
                '    * *      ',
                '  *     *    ',
                ' *       *   ',
                '*         *  ',
                '* * * * * *  ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*         *  '
            ]

        B = [
                '* * * *     ',
                '*       *   ',
                '*        *  ',
                '*       *   ',
                '* * * *     ',
                '*       *   ',
                '*        *  ',
                '*       *   ',
                '* * * *     '
            ]

        C = [
                '   * * *      ',
                ' *       *    ',
                '*         *   ',
                '*             ',
                '*             ',
                '*             ',
                '*         *   ',
                ' *       *    ',
                '   * * *      '
            ]

        D = [
                '* * *        ',
                '*      *     ',
                '*        *   ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*        *   ',
                '*      *     ',
                '* * *        '
            ]

        E = [
                '* * * * *   ',
                '*           ',
                '*           ',
                '*           ',
                '* * * * *   ',
                '*           ',
                '*           ',
                '*           ',
                '* * * * *   '
            ]

        F = [
                '* * * * *   ',
                '*           ',
                '*           ',
                '*           ',
                '* * * * *   ',
                '*           ',
                '*           ',
                '*           ',
                '*           '
            ]

        G = [
                '   * * *      ',
                ' *       *    ',
                '*         *   ',
                '*             ',
                '*             ',
                '*    * * * *  ',
                '*        * *  ',
                ' *       * *  ',
                '   * * *   *  '
            ]

        H = [
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '* * * * * *  ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*         *  '
            ]

        I = [
                '* * * * *   ',
                '    *       ',
                '    *       ',
                '    *       ',
                '    *       ',
                '    *       ',
                '    *       ',
                '    *       ',
                '* * * * *   '
            ]

        J = [
                ' * * * * *  ',
                '     *      ',
                '     *      ',
                '     *      ',
                '     *      ',
                '     *      ',
                '*    *      ',
                '  *  *      ',
                '     *      '
            ]

        K = [
                '*         *  ',
                '*       *    ',
                '*     *      ',
                '*   *        ',
                '* *          ',
                '*   *        ',
                '*     *      ',
                '*       *    ',
                '*         *  '
            ]

        L = [
                '*             ',
                '*             ',
                '*             ',
                '*             ',
                '*             ',
                '*             ',
                '*             ',
                '*             ',
                '* * * * * *   '
            ]

        M = [
                '*         *  ',
                '* *     * *  ',
                '*  *   *  *  ',
                '*   * *   *  ',
                '*    *    *  ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*         *  '
            ]

        N = [
                '*         *  ',
                '* *       *  ',
                '*  *      *  ',
                '*   *     *  ',
                '*    *    *  ',
                '*     *   *  ',
                '*      *  *  ',
                '*       * *  ',
                '*         *  '
            ]

        O = [
                '   * * *     ',
                ' *       *   ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                ' *       *   ',
                '   * * *     '
            ]

        P = [
                '* * * *     ',
                '*       *   ',
                '*        *  ',
                '*       *   ',
                '* * * *     ',
                '*           ',
                '*           ',
                '*           ',
                '*           '
            ]

        Q = [
                '   * * *     ',
                ' *       *   ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*      *  *  ',
                ' *       *   ',
                '   * * *   * '
            ]

        R = [
                '* * * *     ',
                '*       *   ',
                '*        *  ',
                '*       *   ',
                '* * * *     ',
                '*  *        ',
                '*    *      ',
                '*      *    ',
                '*        *  '
            ]

        S = [
                '   * * *     ',
                ' *       *   ',
                '*            ',
                ' *           ',
                '   * * *     ',
                '         *   ',
                '          *  ',
                ' *       *   ',
                '   * * *     '
            ]

        T = [
                '* * * * * * *  ',
                '      *        ',
                '      *        ',
                '      *        ',
                '      *        ',
                '      *        ',
                '      *        ',
                '      *        ',
                '      *        '
            ]

        U = [
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                ' *       *   ',
                '   * * *     '
            ]

        V = [
                '*             *  ',
                '*             *  ',
                '*             *  ',
                '*             *  ',
                '*             *  ',
                '*             *  ',
                '  *         *    ',
                '    *     *      ',
                '       *         '
            ]

        W = [
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*         *  ',
                '*    *    *  ',
                '*   * *   *  ',
                '*  *   *  *  ',
                '* *     * *  ',
                '*         *  '
            ]

        X = [
                '*       *  ',
                ' *     *   ',
                '  *   *    ',
                '   * *     ',
                '    *      ',
                '   * *     ',
                '  *   *    ',
                ' *     *   ',
                '*       *  '
            ]

        Y = [
                '*             *  ',
                '  *         *    ',
                '    *     *      ',
                '      * *        ',
                '       *         ',
                '       *         ',
                '       *         ',
                '       *         ',
                '       *         '
            ]

        Z = [
                '* * * * * * * *  ',
                '             *   ',
                '           *     ',
                '         *       ',
                '       *         ',
                '     *           ',
                '   *             ',
                ' *               ',
                '* * * * * * * *  '
            ]

        sp = [
                '     ',
                '     ',
                '     ',
                '     ',
                '     ',
                '     ',
                '     ',
                '     ',
                '     '
            ]

        return {
                  "A" : A, "B" : B, "C" : C, "D" : D,
                  "E" : E, "F" : F, "G" : G, "H" : H,
                  "I" : I, "J" : J, "K" : K, "L" : L,
                  "M" : M, "N" : N, "O" : O, "P" : P,
                  "Q" : Q, "R" : R, "S" : S, "T" : T,
                  "U" : U, "V" : V, "W" : W, "X" : X,
                  "Y" : Y, "Z" : Z, " " : sp
               }
