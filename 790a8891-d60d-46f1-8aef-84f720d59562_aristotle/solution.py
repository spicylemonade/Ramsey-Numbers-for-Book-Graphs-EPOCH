"""Deterministic constructions for the triangular book graph Ramsey task."""

from itertools import product


def solution(n: int) -> str:
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

    raise NotImplementedError(
        "No deterministic witness is embedded for this n. "
        "The general all-n construction is still open; this implementation "
        "only returns verified witnesses for the documented exact range and "
        "the published prime-power family."
    )


def _exact_witness(n: int) -> str | None:
    small = _small_exact_witnesses()
    if n in small:
        return small[n]

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
    }


def _graph6_to_adjacency_string(data: str) -> str:
    values = [ord(char) - 63 for char in data.strip()]
    if not values:
        raise ValueError("empty graph6 string")

    if values[0] != 63:
        order = values[0]
        index = 1
    elif values[1] != 63:
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

    bits: list[str] = []
    total = 2 * q
    for right in range(total):
        for left in range(right):
            left_block, left_pos = divmod(left, q)
            right_block, right_pos = divmod(right, q)
            diff = index[subtract(elements[right_pos], elements[left_pos])]
            if left_block == 0 and right_block == 0:
                edge = diff in residues
            elif left_block == 1 and right_block == 1:
                edge = diff in nonresidues
            else:
                edge = diff in residues
            bits.append("1" if edge else "0")
    return "".join(bits)


def _field_model(
    p: int, k: int
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
