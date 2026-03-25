"""Deterministic constructions for the triangular book graph Ramsey task.

This artifact intentionally does not guess. It returns only:
- embedded exact witnesses backed by published data; or
- the published two-block Paley-type construction when `2n - 1` is a
  prime power congruent to 1 modulo 4.

Unsupported inputs raise ``ValueError`` instead of falling back to
probabilistic search or generated C code.
"""

from __future__ import annotations

import argparse
from itertools import product


def solution(n: int) -> str:
    """Return an adjacency string for a verified witness graph."""
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return "0"

    exact = _exact_witness(n)
    if exact is not None:
        return exact

    q = 2 * n - 1
    prime_power = _prime_power(q)
    if prime_power is not None and q % 4 == 1:
        p, k = prime_power
        return _paley_two_block(q, p, k)

    raise ValueError(
        f"n={n} is unsupported by this deterministic artifact. "
        "Supported inputs are the embedded exact witness range n<=22 and "
        "odd n with 2n-1 a prime power congruent to 1 modulo 4."
    )


def _exact_witness(n: int) -> str | None:
    small = _small_exact_witnesses()
    if n in small:
        return small[n]

    two_block = _exact_two_block_witnesses()
    if n in two_block:
        q, d11, d12 = two_block[n]
        d22 = set(range(1, q)) - set(d11)
        return _cyclic_two_block(q, set(d11), set(d12), d22)

    graph6 = _exact_graph6_witnesses()
    if n in graph6:
        return _graph6_to_adjacency_string(graph6[n])
    return None


def _small_exact_witnesses() -> dict[int, str]:
    return {
        2: "000101110001100",
        4: (
            "110111100000011101001110000100101010010000111000011010000110100011010111"
            "0011000110100010110"
        ),
    }


def _exact_two_block_witnesses() -> dict[int, tuple[int, tuple[int, ...], tuple[int, ...]]]:
    return {
        22: (
            43,
            (
                4,
                6,
                7,
                12,
                13,
                14,
                15,
                16,
                17,
                19,
                21,
                22,
                24,
                26,
                27,
                28,
                29,
                30,
                31,
                36,
                37,
                39,
            ),
            (
                0,
                1,
                3,
                6,
                7,
                8,
                10,
                11,
                12,
                14,
                17,
                24,
                25,
                26,
                28,
                29,
                30,
                34,
                35,
                38,
                41,
            ),
        ),
    }


def _exact_graph6_witnesses() -> dict[int, str]:
    return {
        5: "QCrfbo{iMglRLREhpgYLBgsLPwW",
        6: "UCQebQsU`YPhphWteL[pjREmeH]eHZRCkstJEfhW",
        7: "YCQefRs]dyJsJsiKybJSZLPmYb]Y`ZLOkrSJEY`[XiDgrSJgrSJSXyD_",
        8: "]COceRc{bqFcfcRqC{dEhsYdgtXgt[sYlLEzhgrYebLtLCZtL?ZYecLehjBWtLWZbSt`lEhzBW",
        9: (
            "a?bBDbWzFkNWnWvkLz@nWE|aeg]eg^RSLstFMegwyYb`stf`ssfOyYRsMeCy`sofiFRA^SMaCz"
            "SMaCxiFXA]Y`uOfRSNqCw"
        ),
        10: (
            "e?bBD`WjEkLWlWUkTjElWYt_tj?tjDDeNPXbyJKZgkrfPXfFPXfbgkrwyJCzFPYfK\\Di]WyIS}"
            "WyISzK\\DI]rFPQfUWyISxXbghRarFXQfarFXQfPXb{hR_"
        ),
        11: (
            "i?AEFBo]DwZoZolwZ]FZo|n@z]@z]?|n?NZoiebMiYKlSsZLSs^eiYNxie`zLSsNKtRO{Xie`"
            "{Xie`yKtRO}bLScNsXic`zPeiQFebLScNebLOcNRPegQFssXiC`yebLocNiYKvAO|SsX}C`w"
        ),
        12: (
            "m?AEFBo}BwVovoZwU}Evoz^Bu}Fu}Bz^?}voFu}?^ZwUjGbujGbzTcPmtXCxujGnFYka}MtX@y"
            "MtX@xFYk_{PujGNaMtX@yGzTcFcPujGNcPujGNqGzScFkaMtH@|cPu`GNUPFYC_}kaMoH@ykaM"
            "wH@|UPF[C_~TcPv@GNYkaNwH@w"
        ),
        13: (
            "q?AEF@omAwTotoyw]mBtonV@]mD]mEnVBjto\\]m@tywBjtoBjto`lXEwZUPjBYqNkLjG~WZUPz"
            "WZUPxkLjG{ZBYqNbWZUPyL`lXFcZBYyNcZBYiNqL`lDFkbWZPP|cZBWINUPkLog}kbWY`P}kbW"
            "Y`PzUPkLOg}tcZASINukbWA`PzYqLaIDFetcZKSINEtcZ[SINBYqL}IDF_"
        ),
        14: (
            "u?AADBOyFg^O^OngZyB^Ol|BZyFZyFl|Bz^O^ZyD|ngJz^OJz^OD|ng@^ZyDSrJBtRKkNieXWZi"
            "eXWxtRKk{\\SrJNBieX\\{MiXdVw\\SrGnW\\SrGnkMiX_VjBieWDxW\\Sr_nd`tRIA~JBieCDzJ"
            "BiecDxd`tRQA}XW\\Sc_nrJBi_cDzKkMiAOVeXW\\SC_neXW\\SC_nRKkMiAOVsrJBi_cDyeXW\\"
            "sC_niXd`vOQA|SrJB}_cDw"
        ),
        15: (
            "y?AADBOyBgVOvOZgUyEvOZ\\AuyEuyBZ\\AuvOuuyFZZgMuvOmuvOVZZgDuuy?muvOAzZ\\AIfMO}"
            "IfMO~DRfG^pSxqF]IfMPxwi[xFbpSxqnBpSxqn`wi[wVg]IfMDxBpSxwncNDRea~G]IfHD~G]If"
            "HDzcNDRca{xBpSxGnfG]IfHD}[`wiScV{xBpSHGn[xBpTHGnM[`wiccVrfG]IHHDy[xBpPHGnh"
            "rcNDCca|RfG]IHHD|RfG]IHHDyhrcNLCca{i[xBvPHGnDRfG^yHHDw"
        ),
        16: (
            "}??CEB_[DoZ_z_\\oV[Ez_zmBv[Bv[DzmB]z_zv[Bn\\oV]z_v]z_zn\\oMzv[@v]z_F\\zm?Mzv[?"
            "Mzv[DQYVG^SedqFycsmO~iRQxBnSedqNNSedq^FiRQxN`ycsmR{NSedo^O|QYVP{`ycsmb{`yc"
            "skb}O|QYSP~cNSedC^[`ycsgb|qFiROaNjcNSe`C^JcNSe`C^dqFiROaNh[`ycsGb|JcNSc`C^"
            "smO|QACP|h[`ydCGbxh[`ydCGb{smO|OaCP|LJcNSG`C^Hh[`ypCGb{edqFjCOaNhLJcN]G`C^h"
            "LJcN]G`C^SedqF~COaN_"
        ),
        17: (
            "~?@A??CEB_[DoZ_Z_loZ[FZ_\\m?z[Cz[E\\mBfZ_[z[DrloZfZ_ZfZ_lrloZ[z[FZfZ_\\m\\m?z[z"
            "[?z[z[?\\m\\m?FZfZ_kLTJW]otSl`|`ihZB\\`ihZFMotSlfbkLTJZw\\`ihZ^`uEidh~BkLTJBzB"
            "kLTJb|`uEidP~W\\`ihC^ZBkLTKb|kMotSQNjW\\`igc^JW\\`igc^dkMotSQNhZBkLVCb|JW\\`i"
            "Wc^Sl`uEhaP}hZBkLBCbyhZBkLbCb|Sl`uEPaP|TJW\\`cWc^ihZBkKbCb}idkMoQKQNlTJW\\_"
            "cWc^LTJW\\_cWc^EidkMsQKQN`ihZBnCbCb{LTJW\\wcWc^otSl`vaPaP|`ihZB~CbCbw"
        ),
        18: (
            "~?@E??CAA_sFO]_]_nOZsF]_\\yAzsEzsB\\yAv]_uzsFZnOMv]_mv]_vZnO\\uzsFmv]_]z\\yA|uz"
            "sA|uzs@]z\\y?Vmv]_A|uzs?JvZnOQHjEmFqHjEmFxCtbVB}PLWtozqHjEmNNGekYx{]PLWtrw]"
            "PLWtz{NGekYt~BqHjEh^w]PLWsJz`xCtbOnvBqHjE`^VBqHjE`^j`xCtaOnyw]PLWCJzVBqHjG`"
            "^L[NGekaD{Yw]PLXCJ{Yw]PLXCJ}L[NGecaD|bVBqHhG`^kYw]PKHCJypj`xCwcOntbVBqHPG`^"
            "tbVBqGPG`^Ypj`xCGcOnekYw]PAHCJ{tbVBqGPG`^RUL[NG`CaD{ekYw]TAHCJwekYw]\\AHCJ"
            "{RUL[NM`CaD|CtbVBvgPG`^GekYw^|AHCJw"
        ),
        19: (
            "~?@I??CAA_sFO]_]_nOZsB]_LyAZsEZsFLyBr]_]Zs@xnORr]_rr]_XxnOU]ZsErr]_zNLyBu]Z"
            "sBu]ZsDzNLy@]rr]_Ju]Zs?nXxnO@]rr]_@]rr]_gjUMJHyItbaq^PUk[UR\\DYppX[yItbar{"
            "yItbary\\DYppX{fPUk[V^cyItbaj}RgjUMGnkfPUk[P^kfPUk[@^URgjUMOndcyItbcJwkfPUk"
            "[`^aq\\DYpqD~DcyItbcJ~DcyIt`cJzaq\\DYoqD{wkfPUkK`^FDcyIt`cJ{[URgjUEOnwwkfPU"
            "kK`^WwkfPUkK`^k[URgjEEOnjFDcyIx`cJ|WwkfPTKK`^tbaq\\DCoqD|jFDcyIH`cJ|jFDcyG"
            "H`cJytbaq\\ECoqD}lWwkfO`KK`^TjFDcySH`cJxUk[URjOeEOnalWwkf]`KK`^alWwkf]`KK`^"
            "PUk[UR~OeEOn_"
        ),
        20: (
            "~?@M???CB?wF_N?n?v_\\wBn?m{@\\wD\\wEm{Bjn?|\\wBtv_Vjn?Vjn?jtv_Y|\\wFVjn?\\]m{Ay|"
            "\\wEy|\\wF\\]m{BvVjn?]y|\\w@zjtv_BvVjn?BvVjn?@zjtv_?]y|\\wDcLWuaruOtbYJNk`jEsU"
            "Zk`jEsUxuOtbYJ}\\cLWua~rk`jEsVzMqEkZP^u\\cLWu_~U\\cLWu_~JMqEkZO^ark`jEuF{U\\"
            "cLWuO~PXuOtbXB}ark`jEaF}ark`jEaFzPXuOtbPB}sU\\cLWsO~uark`jAaFzYJMqEkIG^esU"
            "\\cLWSO~EsU\\cLWSO~bYJMqEkIG^wuark`hAaFzEsU\\cLgSO~kZPXuOq`PB|Wuark`dAaF|Wua"
            "rk`DAaF}kZPXuOa`PB|jEsU\\cGgSO~LWuark`DAaFwtbYJMqCSIG^`jEsU\\cGgSO~`jEsU\\cG"
            "gSO~OtbYJMuCSIG^cLWuarn`DAaF{`jEsU\\{GgSO~qEkZPXvoa`PB|cLWuar~`DAaFw"
        ),
        21: (
            "~?@Q???CB?wF_^?^?N_RwE^?X{ArwArwDX{BU^?yrwFjN_NU^?nU^?VjN_TyrwEnU^?Y|X{?tyrw"
            "CtyrwEY|X{BenU^?{tyrwFrVjN_NenU^?NenU^?FrVjN_@{tyrw?NenU^??}Y|X{AdRWrUS]dR"
            "WrUS^QhkXjILsiZEYqfMdRWrUTwyTLbLX^psiZEYq~PsiZEYq~gyTLbLW^iMdRWrUFxPsiZEYo"
            "~dFQhkXiB~IMdRWrSFzIMdRWr[F|dFQhkXeB|XPsiZEX_~jIMdRWrKF}kgyTLbCo^lXPsiZEh_"
            "~LXPsiZEh_~ekgyTLaSo^xjIMdRWDKFzLXPsiZ?h_~KtdFQhlAeB{XjIMdRYDKF{XjIMdRYDKF"
            "}KtdFQhdAeB|bLXPsiXOh_~kXjIMdRIDKF}pekgyTKgSo^lbLXPsiXOh_~LbLXPsiXOh_~epek"
            "gySKgSo^hkXjIMdBIDKF|LbLXPs_XOh_~SuKtdFR@dAeB}hkXjIMeBIDKFyhkXjIMmBIDKFxSu"
            "KtdF^@dAeB}TLbLXPvoXOh_~QhkXjIN}BIDKFw"
        ),
    }


def _graph6_to_adjacency_string(data: str) -> str:
    values = [ord(char) - 63 for char in data.strip()]
    if not values:
        raise ValueError("empty graph6 string")

    if values[0] != 63:
        order = values[0]
        index = 1
    elif len(values) >= 4 and values[1] != 63:
        order = (values[1] << 12) | (values[2] << 6) | values[3]
        index = 4
    else:
        raise ValueError("graph6 order encoding above 258047 is unsupported")

    need = order * (order - 1) // 2
    bits: list[str] = []
    for value in values[index:]:
        for shift in range(5, -1, -1):
            bits.append("1" if (value >> shift) & 1 else "0")

    if len(bits) < need:
        raise ValueError("graph6 payload is truncated")
    return "".join(bits[:need])


def _prime_power(q: int) -> tuple[int, int] | None:
    for p in range(2, q + 1):
        if not _is_prime(p):
            continue
        value = p
        exponent = 1
        while value < q:
            value *= p
            exponent += 1
        if value == q:
            return p, exponent
    return None


def _is_prime(p: int) -> bool:
    if p < 2:
        return False
    if p % 2 == 0:
        return p == 2
    divisor = 3
    while divisor * divisor <= p:
        if p % divisor == 0:
            return False
        divisor += 2
    return True


def _paley_two_block(q: int, p: int, k: int) -> str:
    elements, subtract, multiply, zero = _field_model(p, k)
    index = {element: idx for idx, element in enumerate(elements)}

    residues: set[int] = set()
    for element in elements:
        if element == zero:
            continue
        residues.add(index[multiply(element, element)])

    zero_index = index[zero]
    nonresidues = set(range(q)) - residues - {zero_index}

    def diff_fn(right_pos: int, left_pos: int) -> int:
        return index[subtract(elements[right_pos], elements[left_pos])]

    return _cyclic_two_block(q, residues, residues, nonresidues, diff_fn=diff_fn)


def _cyclic_two_block(
    q: int,
    d11: set[int],
    d12: set[int],
    d22: set[int],
    diff_fn=None,
) -> str:
    if diff_fn is None:
        def diff_fn(right_pos: int, left_pos: int) -> int:
            return (right_pos - left_pos) % q

    bits: list[str] = []
    total = 2 * q
    for right in range(total):
        for left in range(right):
            left_block, left_pos = divmod(left, q)
            right_block, right_pos = divmod(right, q)
            diff = diff_fn(right_pos, left_pos)
            if left_block == 0 and right_block == 0:
                edge = diff in d11
            elif left_block == 1 and right_block == 1:
                edge = diff in d22
            else:
                edge = diff in d12
            bits.append("1" if edge else "0")
    return "".join(bits)


def _field_model(
    p: int,
    k: int,
) -> tuple[
    list[tuple[int, ...]],
    callable,
    callable,
    tuple[int, ...],
]:
    if k == 1:
        elements = [(value,) for value in range(p)]
        zero = (0,)

        def subtract(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
            return ((a[0] - b[0]) % p,)

        def multiply(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
            return ((a[0] * b[0]) % p,)

        return elements, subtract, multiply, zero

    modulus = _find_irreducible_polynomial(p, k)
    elements = [tuple(coeffs) for coeffs in product(range(p), repeat=k)]
    zero = tuple(0 for _ in range(k))

    def subtract(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        return tuple((a[idx] - b[idx]) % p for idx in range(k))

    def multiply(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        temp = [0] * (2 * k - 1)
        for i, a_coeff in enumerate(a):
            if a_coeff == 0:
                continue
            for j, b_coeff in enumerate(b):
                if b_coeff == 0:
                    continue
                temp[i + j] = (temp[i + j] + a_coeff * b_coeff) % p

        for degree in range(2 * k - 2, k - 1, -1):
            coeff = temp[degree]
            if coeff == 0:
                continue
            for idx, mod_coeff in enumerate(modulus):
                temp[degree - k + idx] = (temp[degree - k + idx] - coeff * mod_coeff) % p
        return tuple(value % p for value in temp[:k])

    return elements, subtract, multiply, zero


def _find_irreducible_polynomial(p: int, k: int) -> list[int]:
    for coeffs in product(range(p), repeat=k):
        candidate = list(coeffs)
        if _is_irreducible(candidate, p):
            return candidate
    raise ValueError(f"no irreducible polynomial found for GF({p}^{k})")


def _is_irreducible(coeffs: list[int], p: int) -> bool:
    degree = len(coeffs)
    polynomial = coeffs[:] + [1]
    for divisor_degree in range(1, degree // 2 + 1):
        for divisor_coeffs in product(range(p), repeat=divisor_degree):
            divisor = list(divisor_coeffs) + [1]
            if _polynomial_mod(polynomial, divisor, p) == [0]:
                return False
    return True


def _polynomial_mod(poly: list[int], mod_poly: list[int], p: int) -> list[int]:
    remainder = poly[:]
    while len(remainder) >= len(mod_poly):
        coeff = remainder[-1] % p
        if coeff:
            shift = len(remainder) - len(mod_poly)
            for idx, mod_coeff in enumerate(mod_poly):
                remainder[shift + idx] = (remainder[shift + idx] - coeff * mod_coeff) % p
        remainder.pop()
    return _trim_polynomial(remainder)


def _trim_polynomial(poly: list[int]) -> list[int]:
    trimmed = poly[:]
    while len(trimmed) > 1 and trimmed[-1] == 0:
        trimmed.pop()
    return trimmed


def _verify_book_constraints(adjacency: str, n: int) -> tuple[bool, str]:
    order = 4 * n - 2
    expected = order * (order - 1) // 2
    if len(adjacency) != expected:
        return False, f"wrong length: got {len(adjacency)}, expected {expected}"

    neighbors = [0] * order
    idx = 0
    for right in range(order):
        for left in range(right):
            bit = adjacency[idx]
            idx += 1
            if bit == "1":
                neighbors[left] |= 1 << right
                neighbors[right] |= 1 << left
            elif bit != "0":
                return False, f"invalid bit {bit!r} at position {idx - 1}"

    full_mask = (1 << order) - 1
    nonneighbors = [
        (~neighbors[vertex]) & (full_mask ^ (1 << vertex))
        for vertex in range(order)
    ]

    for right in range(order):
        for left in range(right):
            common_neighbors = (neighbors[left] & neighbors[right]).bit_count()
            edge = (neighbors[left] >> right) & 1
            if edge:
                if common_neighbors > n - 2:
                    return (
                        False,
                        f"edge ({left},{right}) has {common_neighbors} common neighbors",
                    )
            else:
                common_nonneighbors = (
                    nonneighbors[left] & nonneighbors[right]
                ).bit_count()
                if common_nonneighbors > n - 1:
                    return (
                        False,
                        f"non-edge ({left},{right}) has {common_nonneighbors} common non-neighbors",
                    )
    return True, "ok"


def _supported_values(limit: int) -> tuple[list[int], list[int]]:
    supported: list[int] = []
    unsupported: list[int] = []
    for n in range(1, limit + 1):
        try:
            adjacency = solution(n)
        except ValueError:
            unsupported.append(n)
            continue

        check_again = solution(n)
        if adjacency != check_again:
            raise AssertionError(f"solution({n}) is not deterministic")

        ok, message = _verify_book_constraints(adjacency, n)
        if not ok:
            raise AssertionError(f"solution({n}) failed verification: {message}")
        supported.append(n)
    return supported, unsupported


def _main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="?", type=int, help="emit a witness for this n")
    parser.add_argument(
        "--verify-supported",
        action="store_true",
        help="verify every supported value up to --limit",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="upper bound used by --verify-supported",
    )
    args = parser.parse_args()

    if args.n is not None:
        print(solution(args.n))
        return

    if args.verify_supported:
        supported, unsupported = _supported_values(args.limit)
        print(f"supported up to {args.limit}: {supported}")
        print(f"unsupported up to {args.limit}: {unsupported}")
        return

    parser.print_help()


if __name__ == "__main__":
    _main()
