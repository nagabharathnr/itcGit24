package org.scalatasknag.com

import org.apache.spark.SparkContext
import org.apache.spark.sql.functions

object Main {
  def main(args: Array[String]): Unit = {

    val tm = new SparkContext("local[1]", "highTM")

    //val rdd5 = tm.textFile("A:\\Scala_projects\\ScalaTaskNag\\src\\main\\scala\\sam_temp")
    val rdd5 = tm.textFile("A:\\Scala_projects\\ScalaTaskNag\\input\\data1.txt")
    val rdd6 = rdd5.map(x => x.split(",")(2))
    val rdd7 = rdd6.max
    println("Max temperature is: " +rdd7)

    //rdd7.collect().foreach(println)
    //rdd6.saveAsTextFile("A:\\Scala_projects\\ScalaTaskNag\\output\\output1.txt")
  }

}
