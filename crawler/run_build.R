# 运行中考真题题库生成
cmd <- "python \"f:\\2026年\\梦见2026年\\蕊总资料\\crawler\\build_real_exam_bank.py\""
res <- system(cmd, intern = TRUE)
cat(paste(res, collapse = "\n"))

