package org.scalatasknag.com

import org.apache.spark.SparkContext

object Main1 {
  def main(args: Array[String]): Unit = {

    val tm1 = new SparkContext("local[1]", "cnt")

    val rdd8 = tm1.textFile("A:\\Scala_projects\\ScalaTaskNag\\src\\main\\scala\\sam_temp")
    //val rdd9 = rdd8.map(x => { val rdd10 = x.split(",")(rdd10(0), rdd10(2).toDouble)})

    //val res = rdd9.filter{case(_, temperature) => temperature > 50.0}.count()
    val rdd6 = rdd8.map(x => {
      val columns = x.split(",")
      val sensor = columns(0)
      val temp = columns(columns.length - 1).toDouble
      (sensor, temp)
    })

    val res = rdd6.filter { case (_, temp) => temp > 50.0 }
      .map(sen => (sen._1, 1))
      .reduceByKey(_ + _)
    res.collect().foreach{case (sensor, temp) =>
      println(sensor, temp)}

    //println("Count of sensor names with temperatures above 50.0: "+ res)
    //println("count is: " +res)

  }

}
