# Civil law simulation

## A.1 — rule_based

**Prompt**
```
Considering the following facts:
1. Trong Đơn khởi kiện đề ngày 10/8/2015, Đơn khởi kiện bổ sung đề ngày 20/3/2017, các bản khai, biên bản lấy lời khai, Tờ trình về di chúc ngày 07/12/2016, Biên bản về kiểm tra việc giao nộp tiếp cận công khai chứng cứ ngày 19/6/2018, Biên bản hòa giải không thành ngày 19/6/2018, nguyên đơn là ông NVP trình bày là Căn nhà số 161G BVĐ, Phường 6, Quận 4, Thành phố Hồ Chí Minh là của cha mẹ ông là ông NVL và bà BTH, cha ông chết vào năm 1977, mẹ ông chết năm 2011, ông bà nội và ông bà ngoại của ông …
2. Ông Ph xác định có 10 người (anh chị em) được hưởng tài sản chung và được chia thừa kế là: 1. Bà BMJ 2. Ông NVH 3. Ông NVP 4. Bà NNS 5. Ông NVN 6. Bà NTT 7. Bà NTN 8. Bà NTL 9. Ông NTM 10. Bà BTTH
3. Theo Biên bản hòa giải không thành ngày 19/6/2018, ông Ph đã rút yêu cầu Tòa án tuyên Bản di chúc của mẹ ông lập ngày 22/5/2006 bị vô hiệu, ông đề nghị tất cả không tính phần công sức đóng góp trước đây và yêu cầu chia đều giá trị di sản của cha mẹ cho 10 người con. Di chúc của mẹ ông như đã nêu trên là hợp pháp thì ông công nhận và đề nghị chia theo quy định của pháp luật trên số tài sản còn lại.
4. Theo các bản khai, biên bản lấy lời khai, Tờ giải trình ngày 07/12/2016, Biên bản về kiểm tra việc giao nộp tiếp cận công khai chứng cứ ngày 19/6/2018, Biên bản hòa giải không thành ngày 19/6/2018, bị đơn là bà NNS trình bày về quan hệ nhân thân thì đúng như ông NVP đã trình bày, bà xác nhận di sản để chia thừa kế và chia tài sản chung của cha mẹ để lại là Căn nhà số 161G BVĐ, Phường 6, Quận 4, TP Hồ Chí Minh. Cha bà là ông NVL sinh năm 1920 và chết vào năm 1977, mẹ bà là bà BTH sinh năm 1926 …
5. Theo các bản khai, biên bản lấy lời khai, Đơn giải trình ngày 07/12/2016, Biên bản về kiểm tra việc giao nộp tiếp cận công khai chứng cứ ngày 19/6/2018, Biên bản hòa giải không thành ngày 19/6/2018, người có quyền lợi nghĩa vụ liên quan là ông NVH trình bày về quan hệ nhân thân thì đúng như ông Ph và bà S đã trình bày, ông xác nhận di sản để chia thừa kế và chia tài sản chung của cha mẹ để lại thì đúng như ông Ph bà S trình bày. Cha ông là ông NVL, mẹ ông là bà BTH có năm sinh và năm chết như …
6. Theo các bản khai, biên bản lấy lời khai, Tờ trình về di chúc ngày 07/12/2016, Biên bản về kiểm tra việc giao nộp tiếp cận công khai chứng cứ ngày 19/6/2018, Biên bản hòa giải không thành ngày 19/6/2018, người có quyền lợi nghĩa vụ liên quan là các ông bà NTT, NTN , NVN (do bà S đại diện theo ủy quyền), BTTH, trình bày về quan hệ nhân thân thì đúng như ông Ph và bà S đã trình bày, các ông bà xác nhận di sản để chia thừa kế và chia tài sản chung của cha mẹ để lại thì đúng như ông Ph bà S trình …
7. Theo các bản khai, biên bản lấy lời khai, Tờ trình về di chúc ngày 06/12/2016, Biên bản về kiểm tra việc giao nộp tiếp cận công khai chứng cứ ngày 19/6/2018, Biên bản hòa giải không thành ngày 19/6/2018, người có quyền lợi nghĩa vụ liên quan là các ông bà NTM , BMJ (do ông Ph đại diện theo ủy quyền), NTL trình bày là thống nhất với phần trình bày của ông Ph. Theo Biên bản về kiểm tra việc giao nộp tiếp cận công khai chứng cứ ngày 19/6/2018, Biên bản hòa giải không thành ngày 19/6/2018, người có …
8. Tại phiên tòa,
9. - Ý kiến của nguyên đơn:
10. + Xác nhận ông bà nội, ông bà ngoại của nguyên đơn là đã chết trước cha mẹ của nguyên đơn. Ông VHT và ông LVP là 02 người em rể của nguyên đơn, hiện cư trú tại 161G BVĐ, Phường 6, Quận 4, Thành phố H.
11. + Di sản của cha để lại là ½ Căn nhà 161G BVĐ, Phường 6, Quận 4, TP H thì nguyên đơn xác nhận là tài sản chung, chưa chia và không tranh chấp. Đề nghị tất cả anh chị em không tính phần công sức đóng góp trước đây vào căn nhà này.
12. + Xác định một lần nữa là không yêu cầu Tòa án tuyên Bản di chúc ngày 22/5/2006 của bà BTH bị vô hiệu nhưng nguyên đơn vẫn yêu cầu chia đều giá trị di sản cho 10 anh chị em như đã nêu trên. Mặc dù, nguyên đơn vẫn biết ông NVH được hưởng thừa kế theo di chúc sẽ có phần hưởng di sản nhiều hơn nhưng ông vẫn yêu cầu chia đều là để thể hiện tính công bằng trong gia đình.
13. + Đề nghị chia di sản nêu trên không chia theo hiện vật mà chia theo giá trị. Giá trị di sản nêu trên (Căn nhà 161G BVĐ, Phường 6, Quận 4, Thành phố H) là 6.369.539.358 đồng theo Biên bản định giá ngày 10/11/2017 của Hội đồng định giá. Với trị giá căn nhà nêu trên thì mỗi người sẽ nhận 1/10 giá trị, cụ thể là mỗi người được hưởng 636.953.935,80 đồng tương đương 636.953.936 đồng. Ông xin được nhận nhà này và sẽ thanh toán tiền nêu trên cho 09 anh chị em còn lại, nếu không thì yêu cầu phát mãi …
14. + Khi định giá nhà, nguyên đơn đã tạm ứng 2.000.000 đồng để thanh toán cho thành viên Hội đồng định giá. Nguyên đơn tự chịu 200.000 đồng và yêu cầu mỗi người được hưởng di sản còn lại pH thanh toán cho nguyên đơn 200.000 đồng.
15. - Ý kiến của bị đơn có đại diện theo ủy quyền là bà NTT: Không đồng ý chia đều giá trị di sản cũng như để ông NVP nhận căn nhà nêu trên mà khi chia pH tính đến Bản di chúc ngày 22/5/2006 của mẹ bị đơn. Bị đơn không đồng ý phát mãi nhà để chia đều vì trong các anh chị em còn lại có người muốn nhận nhà. Với cách chia có tính đến di chúc, ông Ph hưởng di sản ít nên không được nhận nhà, còn những ý kiến khác của ông Ph tại phiên tòa này thì bị đơn đồng ý.
16. - Ý kiến của người có quyền lợi, nghĩa vụ liên quan là ông NVH: xác định là ông sẽ nhận phần di sản mà mẹ ông đã để lại theo di chúc cho ông và ông thống nhất với ý kiến của đại diện bị đơn nhưng ông H xin nhận nhà và cam kết thanh toán tiền theo phần cho anh chị em không nhận nhà.
17. - Ý kiến của người có quyền lợi, nghĩa vụ liên quan là các bà NTT, NTN và BTTH: thống nhất với ý kiến của đại diện bị đơn và ông NVH.
18. - Ý kiến của người có quyền lợi, nghĩa vụ liên quan là các ông bà NTM , BMJ do ông Ph đại diện theo ủy quyền: thống nhất với ý kiến của nguyên đơn.
19. - Ý kiến của người có quyền lợi, nghĩa vụ liên quan là bà NTL : Bà thừa nhận Bản di chúc ngày 22/5/2006 của mẹ bà là đúng pháp luật và thống nhất với ý kiến của nguyên đơn.
20. - Ý kiến thêm của bị đơn có đại diện theo ủy quyền là bà NTT: thống nhất với ý kiến của ông NVH.
21. - Ý kiến của các ông bà BMJ, NVH, NVP, NNS, NTT, NTN , NTL , NTM , BTTH xác định là các ông bà NNS, NTT, NTN , BTTH, VHT và LVP hiện nay đang ở tại Căn nhà 161G BVĐ, Phường 6, Quận 4, Thành phố TP H.
22. Ý kiến của đại diện Viện kiểm sát nhân dân Thành phố Hồ Chí Minh:
23. Thẩm phán, Hội đồng xét xử, đương sự đã tuân thủ đúng các quy định Bộ luật tố tụng dân sự năm 2015. Về nội dung vụ án thì nguyên đơn rút yêu cầu Tòa án tuyên Bản di chúc ngày 22/5/2006 của bà BTH bị vô hiệu thì đề nghị Hội đồng xét xử đình chỉ yêu cầu này. Việc các đương sự đồng ý không tính phần công sức đóng góp trước đây của các đương sự vào Căn nhà 161G BVĐ, Phường 6, Quận 4, TP H thì đề nghị Hội đồng xét xử ghi nhận ý kiến này. Căn cứ Bản di chúc ngày 22/5/2006 của bà BTH thì ông H được …
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 659. Phân chia di sản theo di chúc. 1. Việc phân chia di sản được thực hiện theo ý chí của người để lại di chúc; nếu di chúc không xác định rõ phần của từng người thừa kế thì di sản được chia đều cho những người được chỉ định trong di chúc, trừ trường hợp có thoả thuận khác. 2. Trường hợp di chúc xác định phân chia di sản theo hiện vật thì người thừa kế được nhận hiện vật kèm theo hoa lợi, lợi tức thu được từ hiện vật đó hoặc phải chịu phần giá trị của hiện vật bị giảm sút tính đến thời điểm phân chia di sản; nếu hiện vật bị tiêu huỷ do lỗi của người khác thì người thừa kế có quyền yêu cầu bồi thường thiệt hại. 3. Trường hợp di chúc chỉ xác định phân chia di sản theo tỷ lệ đối với tổng giá trị kh
2. [BLDS 2015] Điều 661. Hạn chế phân chia di sản. Trường hợp theo ý chí của người lập di chúc hoặc theo thoả thuận của tất cả những người thừa kế, di sản chỉ được phân chia sau một thời hạn nhất định thì chỉ khi đã hết thời hạn đó di sản mới được đem chia. Trường hợp yêu cầu chia di sản thừa kế mà việc chia di sản ảnh hưởng nghiêm trọng đến đời sống của bên vợ hoặc chồng còn sống và gia đình thì bên còn sống có quyền yêu cầu Tòa án xác định phần di sản mà những người thừa kế được hưởng nhưng chưa cho chia di sản trong một thời hạn nhất định. Thời hạn này không quá 03 năm, kể từ thời điểm mở thừa kế. Hết thời hạn 03 năm mà bên còn sống chứng minh được việc chia di sản vẫn ảnh hưởng nghiêm trọng đến đời sống của gia 
3. [BLDS 2015] Điều 642. Di chúc bị thất lạc, hư hại. 1. Kể từ thời điểm mở thừa kế, nếu bản di chúc bị thất lạc hoặc bị hư hại đến mức không thể hiện được đầy đủ ý chí của người lập di chúc và cũng không có bằng chứng nào chứng minh được ý nguyện đích thực của người lập di chúc thì coi như không có di chúc và áp dụng các quy định về thừa kế theo pháp luật. 2. Trường hợp di sản chưa chia mà tìm thấy di chúc thì di sản được chia theo di chúc. 3. Trong thời hiệu yêu cầu chia di sản, trường hợp di sản đã chia mà tìm thấy di chúc thì phải chia lại theo di chúc nếu người thừa kế theo di chúc yêu cầu
4. [BLDS 2015] Điều 662. Phân chia di sản trong trường hợp có người thừa kế mới hoặc có người thừa kế bị bác bỏ quyền thừa kế. 1. Trường hợp đã phân chia di sản mà xuất hiện người thừa kế mới thì không thực hiện việc phân chia lại di sản bằng hiện vật, nhưng những người thừa kế đã nhận di sản phải thanh toán cho người thừa kế mới một khoản tiền tương ứng với phần di sản của người đó tại thời điểm chia thừa kế theo tỷ lệ tương ứng với phần di sản đã nhận, trừ trường hợp có thoả thuận khác. 2. Trường hợp đã phân chia di sản mà có người thừa kế bị bác bỏ quyền thừa kế thì người đó phải trả lại di sản hoặc thanh toán một khoản tiền tương đương với giá trị di sản được hưởng tại thời điểm chia thừa kế cho những người thừa
5. [BLDS 2015] Điều 660. Phân chia di sản theo pháp luật. 1. Khi phân chia di sản, nếu có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra thì phải dành lại một phần di sản bằng phần mà người thừa kế khác được hưởng để nếu người thừa kế đó còn sống khi sinh ra được hưởng; nếu chết trước khi sinh ra thì những người thừa kế khác được hưởng. 2. Những người thừa kế có quyền yêu cầu phân chia di sản bằng hiện vật; nếu không thể chia đều bằng hiện vật thì những người thừa kế có thể thoả thuận về việc định giá hiện vật và thoả thuận về người nhận hiện vật; nếu không thoả thuận được thì hiện vật được bán để chia
According to the given rules, please evaluate whether the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Dựa trên các quy định pháp luật Việt Nam được trích dẫn, chúng ta sẽ phân tích từng yêu cầu của nguyên đơn:

1. Yêu cầu chia di sản theo di chúc: 
   - Theo Điều 659 BLDS 2015, việc phân chia di sản được thực hiện theo ý chí của người để lại di chúc. 
   - Tuy nhiên, yêu cầu này cần được xem xét kỹ lưỡng về nội dung di chúc và các thỏa thuận giữa các thừa kế.
   - Theo Điều 661 BLDS 2015, nếu yêu cầu chia di sản ảnh hưởng nghiêm trọng đến đời sống của bên vợ/chồng còn sống và gia đình, bên còn sống có quyền yêu cầu xác định phần di sản mà những người thừa kế được hưởng nhưng chưa cho chia di sản trong một thời hạn nhất định.
   - Vì vậy, yêu cầu này cần được xem xét kỹ lưỡng về vấn đề này.

2. Yêu cầu không tính phần công sức đóng góp trước đây:
   - Theo Điều 661 BLDS 2015, nếu các đương sự đồng ý không tính phần công sức đóng góp trước đây, yêu cầu này có thể được chấp nhận.

3. Yêu cầu chia di sản theo giá trị:
   - Theo Điều 659 BLDS 2015, việc phân chia di sản được thực hiện theo ý chí của người để lại di chúc. 
   - Tuy nhiên, việc chia theo giá trị có thể phù hợp với Điều 660 BLDS 2015 về trường hợp có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra.
   - Do đó, yêu cầu này có thể được chấp nhận.

4. Yêu cầu nhận căn nhà 161G BVĐ:
   - Theo Điều 659 BLDS 2015, việc phân chia di sản được thực hiện theo ý chí của người để lại di chúc.
   - Tuy nhiên, nếu di chúc xác định phân chia di sản theo hiện vật, yêu cầu này có thể không được chấp nhận.
   - Cần xem xét nội dung di chúc cụ thể.

5. Yêu cầu phát mãi căn nhà 161G BVĐ:
   - Theo Điều 659 BLDS 2015, việc phân chia di sản được thực hiện theo ý chí của người để lại di chúc.
   - Tuy nhiên, nếu di chúc xác định phân chia di sản theo hiện vật, yêu cầu này có thể không được chấp nhận.
   - Cần xem xét nội dung di chúc cụ thể.

Kết luận:
Yêu cầu của nguyên đơn được chấp nhận (một phần). Yêu cầu chia di
```

## A.2#1 — abductive (defendant)

**Prompt**
```
Considering the following facts:
1. Trong Đơn khởi kiện đề ngày 10/8/2015, Đơn khởi kiện bổ sung đề ngày 20/3/2017, các bản khai, biên bản lấy lời khai, Tờ trình về di chúc ngày 07/12/2016, Biên bản về kiểm tra việc giao nộp tiếp cận công khai chứng cứ ngày 19/6/2018, Biên bản hòa giải không thành ngày 19/6/2018, nguyên đơn là ông NVP trình bày là Căn nhà số 161G BVĐ, Phường 6, Quận 4, Thành phố Hồ Chí Minh là của cha mẹ ông là ông NVL và bà BTH, cha ông chết vào năm 1977, mẹ ông chết năm 2011, ông bà nội và ông bà ngoại của ông …
2. Ông Ph xác định có 10 người (anh chị em) được hưởng tài sản chung và được chia thừa kế là: 1. Bà BMJ 2. Ông NVH 3. Ông NVP 4. Bà NNS 5. Ông NVN 6. Bà NTT 7. Bà NTN 8. Bà NTL 9. Ông NTM 10. Bà BTTH
3. Theo Biên bản hòa giải không thành ngày 19/6/2018, ông Ph đã rút yêu cầu Tòa án tuyên Bản di chúc của mẹ ông lập ngày 22/5/2006 bị vô hiệu, ông đề nghị tất cả không tính phần công sức đóng góp trước đây và yêu cầu chia đều giá trị di sản của cha mẹ cho 10 người con. Di chúc của mẹ ông như đã nêu trên là hợp pháp thì ông công nhận và đề nghị chia theo quy định của pháp luật trên số tài sản còn lại.
4. Theo các bản khai, biên bản lấy lời khai, Tờ giải trình ngày 07/12/2016, Biên bản về kiểm tra việc giao nộp tiếp cận công khai chứng cứ ngày 19/6/2018, Biên bản hòa giải không thành ngày 19/6/2018, bị đơn là bà NNS trình bày về quan hệ nhân thân thì đúng như ông NVP đã trình bày, bà xác nhận di sản để chia thừa kế và chia tài sản chung của cha mẹ để lại là Căn nhà số 161G BVĐ, Phường 6, Quận 4, TP Hồ Chí Minh. Cha bà là ông NVL sinh năm 1920 và chết vào năm 1977, mẹ bà là bà BTH sinh năm 1926 …
5. Theo các bản khai, biên bản lấy lời khai, Đơn giải trình ngày 07/12/2016, Biên bản về kiểm tra việc giao nộp tiếp cận công khai chứng cứ ngày 19/6/2018, Biên bản hòa giải không thành ngày 19/6/2018, người có quyền lợi nghĩa vụ liên quan là ông NVH trình bày về quan hệ nhân thân thì đúng như ông Ph và bà S đã trình bày, ông xác nhận di sản để chia thừa kế và chia tài sản chung của cha mẹ để lại thì đúng như ông Ph bà S trình bày. Cha ông là ông NVL, mẹ ông là bà BTH có năm sinh và năm chết như …
6. Theo các bản khai, biên bản lấy lời khai, Tờ trình về di chúc ngày 07/12/2016, Biên bản về kiểm tra việc giao nộp tiếp cận công khai chứng cứ ngày 19/6/2018, Biên bản hòa giải không thành ngày 19/6/2018, người có quyền lợi nghĩa vụ liên quan là các ông bà NTT, NTN , NVN (do bà S đại diện theo ủy quyền), BTTH, trình bày về quan hệ nhân thân thì đúng như ông Ph và bà S đã trình bày, các ông bà xác nhận di sản để chia thừa kế và chia tài sản chung của cha mẹ để lại thì đúng như ông Ph bà S trình …
7. Theo các bản khai, biên bản lấy lời khai, Tờ trình về di chúc ngày 06/12/2016, Biên bản về kiểm tra việc giao nộp tiếp cận công khai chứng cứ ngày 19/6/2018, Biên bản hòa giải không thành ngày 19/6/2018, người có quyền lợi nghĩa vụ liên quan là các ông bà NTM , BMJ (do ông Ph đại diện theo ủy quyền), NTL trình bày là thống nhất với phần trình bày của ông Ph. Theo Biên bản về kiểm tra việc giao nộp tiếp cận công khai chứng cứ ngày 19/6/2018, Biên bản hòa giải không thành ngày 19/6/2018, người có …
8. Tại phiên tòa,
9. - Ý kiến của nguyên đơn:
10. + Xác nhận ông bà nội, ông bà ngoại của nguyên đơn là đã chết trước cha mẹ của nguyên đơn. Ông VHT và ông LVP là 02 người em rể của nguyên đơn, hiện cư trú tại 161G BVĐ, Phường 6, Quận 4, Thành phố H.
11. + Di sản của cha để lại là ½ Căn nhà 161G BVĐ, Phường 6, Quận 4, TP H thì nguyên đơn xác nhận là tài sản chung, chưa chia và không tranh chấp. Đề nghị tất cả anh chị em không tính phần công sức đóng góp trước đây vào căn nhà này.
12. + Xác định một lần nữa là không yêu cầu Tòa án tuyên Bản di chúc ngày 22/5/2006 của bà BTH bị vô hiệu nhưng nguyên đơn vẫn yêu cầu chia đều giá trị di sản cho 10 anh chị em như đã nêu trên. Mặc dù, nguyên đơn vẫn biết ông NVH được hưởng thừa kế theo di chúc sẽ có phần hưởng di sản nhiều hơn nhưng ông vẫn yêu cầu chia đều là để thể hiện tính công bằng trong gia đình.
13. + Đề nghị chia di sản nêu trên không chia theo hiện vật mà chia theo giá trị. Giá trị di sản nêu trên (Căn nhà 161G BVĐ, Phường 6, Quận 4, Thành phố H) là 6.369.539.358 đồng theo Biên bản định giá ngày 10/11/2017 của Hội đồng định giá. Với trị giá căn nhà nêu trên thì mỗi người sẽ nhận 1/10 giá trị, cụ thể là mỗi người được hưởng 636.953.935,80 đồng tương đương 636.953.936 đồng. Ông xin được nhận nhà này và sẽ thanh toán tiền nêu trên cho 09 anh chị em còn lại, nếu không thì yêu cầu phát mãi …
14. + Khi định giá nhà, nguyên đơn đã tạm ứng 2.000.000 đồng để thanh toán cho thành viên Hội đồng định giá. Nguyên đơn tự chịu 200.000 đồng và yêu cầu mỗi người được hưởng di sản còn lại pH thanh toán cho nguyên đơn 200.000 đồng.
15. - Ý kiến của bị đơn có đại diện theo ủy quyền là bà NTT: Không đồng ý chia đều giá trị di sản cũng như để ông NVP nhận căn nhà nêu trên mà khi chia pH tính đến Bản di chúc ngày 22/5/2006 của mẹ bị đơn. Bị đơn không đồng ý phát mãi nhà để chia đều vì trong các anh chị em còn lại có người muốn nhận nhà. Với cách chia có tính đến di chúc, ông Ph hưởng di sản ít nên không được nhận nhà, còn những ý kiến khác của ông Ph tại phiên tòa này thì bị đơn đồng ý.
16. - Ý kiến của người có quyền lợi, nghĩa vụ liên quan là ông NVH: xác định là ông sẽ nhận phần di sản mà mẹ ông đã để lại theo di chúc cho ông và ông thống nhất với ý kiến của đại diện bị đơn nhưng ông H xin nhận nhà và cam kết thanh toán tiền theo phần cho anh chị em không nhận nhà.
17. - Ý kiến của người có quyền lợi, nghĩa vụ liên quan là các bà NTT, NTN và BTTH: thống nhất với ý kiến của đại diện bị đơn và ông NVH.
18. - Ý kiến của người có quyền lợi, nghĩa vụ liên quan là các ông bà NTM , BMJ do ông Ph đại diện theo ủy quyền: thống nhất với ý kiến của nguyên đơn.
19. - Ý kiến của người có quyền lợi, nghĩa vụ liên quan là bà NTL : Bà thừa nhận Bản di chúc ngày 22/5/2006 của mẹ bà là đúng pháp luật và thống nhất với ý kiến của nguyên đơn.
20. - Ý kiến thêm của bị đơn có đại diện theo ủy quyền là bà NTT: thống nhất với ý kiến của ông NVH.
21. - Ý kiến của các ông bà BMJ, NVH, NVP, NNS, NTT, NTN , NTL , NTM , BTTH xác định là các ông bà NNS, NTT, NTN , BTTH, VHT và LVP hiện nay đang ở tại Căn nhà 161G BVĐ, Phường 6, Quận 4, Thành phố TP H.
22. Ý kiến của đại diện Viện kiểm sát nhân dân Thành phố Hồ Chí Minh:
23. Thẩm phán, Hội đồng xét xử, đương sự đã tuân thủ đúng các quy định Bộ luật tố tụng dân sự năm 2015. Về nội dung vụ án thì nguyên đơn rút yêu cầu Tòa án tuyên Bản di chúc ngày 22/5/2006 của bà BTH bị vô hiệu thì đề nghị Hội đồng xét xử đình chỉ yêu cầu này. Việc các đương sự đồng ý không tính phần công sức đóng góp trước đây của các đương sự vào Căn nhà 161G BVĐ, Phường 6, Quận 4, TP H thì đề nghị Hội đồng xét xử ghi nhận ý kiến này. Căn cứ Bản di chúc ngày 22/5/2006 của bà BTH thì ông H được …
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 659. Phân chia di sản theo di chúc. 1. Việc phân chia di sản được thực hiện theo ý chí của người để lại di chúc; nếu di chúc không xác định rõ phần của từng người thừa kế thì di sản được chia đều cho những người được chỉ định trong di chúc, trừ trường hợp có thoả thuận khác. 2. Trường hợp di chúc xác định phân chia di sản theo hiện vật thì người thừa kế được nhận hiện vật kèm theo hoa lợi, lợi tức thu được từ hiện vật đó hoặc phải chịu phần giá trị của hiện vật bị giảm sút tính đến thời điểm phân chia di sản; nếu hiện vật bị tiêu huỷ do lỗi của người khác thì người thừa kế có quyền yêu cầu bồi thường thiệt hại. 3. Trường hợp di chúc chỉ xác định phân chia di sản theo tỷ lệ đối với tổng giá trị kh
2. [BLDS 2015] Điều 661. Hạn chế phân chia di sản. Trường hợp theo ý chí của người lập di chúc hoặc theo thoả thuận của tất cả những người thừa kế, di sản chỉ được phân chia sau một thời hạn nhất định thì chỉ khi đã hết thời hạn đó di sản mới được đem chia. Trường hợp yêu cầu chia di sản thừa kế mà việc chia di sản ảnh hưởng nghiêm trọng đến đời sống của bên vợ hoặc chồng còn sống và gia đình thì bên còn sống có quyền yêu cầu Tòa án xác định phần di sản mà những người thừa kế được hưởng nhưng chưa cho chia di sản trong một thời hạn nhất định. Thời hạn này không quá 03 năm, kể từ thời điểm mở thừa kế. Hết thời hạn 03 năm mà bên còn sống chứng minh được việc chia di sản vẫn ảnh hưởng nghiêm trọng đến đời sống của gia 
3. [BLDS 2015] Điều 642. Di chúc bị thất lạc, hư hại. 1. Kể từ thời điểm mở thừa kế, nếu bản di chúc bị thất lạc hoặc bị hư hại đến mức không thể hiện được đầy đủ ý chí của người lập di chúc và cũng không có bằng chứng nào chứng minh được ý nguyện đích thực của người lập di chúc thì coi như không có di chúc và áp dụng các quy định về thừa kế theo pháp luật. 2. Trường hợp di sản chưa chia mà tìm thấy di chúc thì di sản được chia theo di chúc. 3. Trong thời hiệu yêu cầu chia di sản, trường hợp di sản đã chia mà tìm thấy di chúc thì phải chia lại theo di chúc nếu người thừa kế theo di chúc yêu cầu
4. [BLDS 2015] Điều 662. Phân chia di sản trong trường hợp có người thừa kế mới hoặc có người thừa kế bị bác bỏ quyền thừa kế. 1. Trường hợp đã phân chia di sản mà xuất hiện người thừa kế mới thì không thực hiện việc phân chia lại di sản bằng hiện vật, nhưng những người thừa kế đã nhận di sản phải thanh toán cho người thừa kế mới một khoản tiền tương ứng với phần di sản của người đó tại thời điểm chia thừa kế theo tỷ lệ tương ứng với phần di sản đã nhận, trừ trường hợp có thoả thuận khác. 2. Trường hợp đã phân chia di sản mà có người thừa kế bị bác bỏ quyền thừa kế thì người đó phải trả lại di sản hoặc thanh toán một khoản tiền tương đương với giá trị di sản được hưởng tại thời điểm chia thừa kế cho những người thừa
5. [BLDS 2015] Điều 660. Phân chia di sản theo pháp luật. 1. Khi phân chia di sản, nếu có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra thì phải dành lại một phần di sản bằng phần mà người thừa kế khác được hưởng để nếu người thừa kế đó còn sống khi sinh ra được hưởng; nếu chết trước khi sinh ra thì những người thừa kế khác được hưởng. 2. Những người thừa kế có quyền yêu cầu phân chia di sản bằng hiện vật; nếu không thể chia đều bằng hiện vật thì những người thừa kế có thể thoả thuận về việc định giá hiện vật và thoả thuận về người nhận hiện vật; nếu không thoả thuận được thì hiện vật được bán để chia
Please suggest hypotheses to support why the outcome of the case might be the court rejects all of the plaintiff's claims.
```
**Response**
```
Để xác định liệu yêu cầu của nguyên đơn có được chấp nhận hay không, chúng ta cần phân tích từng yếu tố từ các tài liệu cung cấp:

1. **Di chúc của mẹ ông NVP**: Theo Biên bản hòa giải không thành ngày 19/6/2018, ông Ph đã rút yêu cầu vô hiệu di chúc của mẹ ông và đề nghị chia đều giá trị di sản. Tuy nhiên, ông Ph vẫn yêu cầu chia đều giá trị di sản, mặc dù ông biết ông NVH sẽ hưởng phần lớn di sản theo di chúc.

2. **Quyền lợi của các anh chị em**: Theo các bản khai, biên bản lấy lời khai, các anh chị em đều xác nhận di sản để chia thừa kế và chia tài sản chung của cha mẹ để lại là căn nhà số 161G BVĐ, Phường 6, Quận 4, TP.HCM. Họ đồng ý không tính phần công sức đóng góp trước đây vào căn nhà này.

3. **Ý kiến của bị đơn**: Bà NTT không đồng ý chia đều giá trị di sản cũng như để ông NVP nhận căn nhà. Bà NTT đề nghị chia theo di chúc của mẹ, với ông Ph hưởng ít hơn.

4. **Ý kiến của các đương sự khác**: Các ông bà NTT, NTN, NVN, BTTH, NTM, BMJ, NNS, NTL, VHT, LVP đều đồng ý với ý kiến của bà NTT và ông NVH.

5. **Ý kiến của đại diện Viện kiểm sát**: Viện kiểm sát đề nghị chia di sản theo di chúc của mẹ, với ông Ph hưởng ít hơn.

Từ những phân tích trên, chúng ta có thể đưa ra một số giả thuyết để hỗ trợ cho quyết định của tòa án:

- **Giả thuyết 1**: Theo Điều 659 BLDS 2015, việc phân chia di sản được thực hiện theo ý chí của người để lại di chúc. Tuy nhiên, vì ông Ph đã rút yêu cầu vô hiệu di chúc và đề nghị chia đều giá trị di sản, nên tòa án có thể chấp nhận yêu cầu này. Tuy nhiên, vì ông Ph vẫn yêu cầu chia đều, không tính phần công sức đóng góp trước đây, điều này có thể gây bất lợi cho ông NVH, người được hưởng di sản nhiều hơn theo di chúc. Do đó, tòa án có thể quyết định không chấp nhận yêu cầu chia đều của ông Ph.

- **Giả thuyết 2**: Theo Điều 661 BLDS 2015, nếu di sản chỉ được phân chia sau một thời hạn nhất định, và việc chia di sản ảnh hưởng nghiêm trọng đến đời sống của bên vợ
```

## judge#1 — judge

**Prompt**
```

```
**Response**
```
llm judge rejected all
```

## Result
- outcome: **the court accepts the plaintiff's claims in whole or in part**
- converged: True
- accepted hypotheses: