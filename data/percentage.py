files = ["test_emerald.csv", "test_hopper.csv", "test_sandy.csv"]
#files = ["test_emerald.csv"]
#files = ["test_hopper.csv"]
#files = ["test_sandy.csv"]

worse = open("worse.out", "w")
better = open("better.out", "w")
mkl = open("mkl.out", "w")
carma = open("carma.out", "w")

right = 0
wrong = 0
mkl_sum = 0
carma_sum = 0

for name in files:
    with open(name) as f:
        for line in f:
            fields = line.strip().split(",")[3:] # ignore m,k,n
            if fields[-1] not in ["mkl", "carma"]:
                continue
            carma_score = float(fields[0])
            mkl_score = float(fields[1])
            correct = fields[2]
            predict = fields[3]

            if correct == predict:
                right += 1
            else:
                wrong += 1

            if correct == "mkl":
                mkl_sum += 1
            else:
                carma_sum += 1

            if correct != predict:
                if correct == "mkl":
                    worse.write("%f\n" % (carma_score / mkl_score))
                else:
                    worse.write("%f\n" % (mkl_score / carma_score))
            else:
                if correct == "mkl":
                    better.write("%f\n" % (mkl_score / carma_score))
                else:
                    better.write("%f\n" % (carma_score / mkl_score))

            if predict == "mkl":
                mkl.write("%f\n" % (mkl_score / mkl_score))
            else:
                mkl.write("%f\n" % (carma_score / mkl_score))

            if predict == "mkl":
                carma.write("%f\n" % (mkl_score/carma_score))
            else:
                carma.write("%f\n" % (carma_score/carma_score))





worse.close()
better.close()
mkl.close()
carma.close()

print "right: %d" % right
print "wrong: %d" % wrong
print "acc: %f" % (float(right)/(right+wrong))
print "mkl: %d" % mkl_sum
print "carma: %d" % carma_sum
