# M3 Math Modelling Challenge 2023
# Ride Like the Wind Without Getting Winded: The Growth of E-bike Use

In many cases, e-bikes provide people with a fast, reliable transportation option that comes without the worry of timing public transit, the nuisance of parking, or the stress of traffic congestion. Policy makers are observing these changes with interest and wondering if e-bikes are likely to become part of a more sustainable energy plan by getting more cars off the roads. For this year's MathWorks Math Modeling Challenge problem, teams were asked to consider the factors leading to the growth of e-bike sales and the long-term impact on carbon emissions, traffic congestion, health and wellness, and more. (https://m3challenge.siam.org/archives/2023)

## Table of Contents

* **[Introduction](#introduction)**
* **Section 1: Identifying the Problem**
  *  1.1 [Restatement of the Problem](#restatement-of-the-problem)
  *  1.2 [Assumptions](#assumptions)
  *  1.3 [Model Development](#model-development)
* **Section 2: Results**
  * 2.1 [Model 1: Linear regression model](#linear-regression-model-1)
  * 2.2 [Model 2: Linear regression model (Optimised)](#linear-regression-model-2)
  * 2.3 [Model 3: Linear regression model (Weighted)](#linear-regression-model-3)
* **Section 3: Conclusion**
  * 3.1 [Evaluation](#evaluation)
  * 3.2 [Summary](#summary)

## Introduction
The United States has been revolutionised through technological growth, with iterative developments and innovative achievements in the electronic vehicle industry. With demand concentrated in the electric bicycle industry, it's important to consider just how important e-bikes are in a long-term future prioritising sustainability, environmental awareness, and general welfare. Posing a viable solution to the environmental crises plaguing not just the United States, but the entire world, projecting future e-bike sales provides invaluable information for government policy. Will e-bikes become a part of a more sustainable energy plan, considering tax incentives and/or investment in bike lane infrastructure? This model will predict the growth in e-bike sales in both two and five years from now, allowing the government to develop both short-term and long-term policies to complement this exponentially growing industry.

## Restatement of the Problem

In context of the problem, we aim to apply a mathematical model using historical data to predict the number of e-bike sales in the United States. We will predict the sales for both 2025 and 2028; both a two year and five year foresight will be useful in demonstrating whether the e-bike market is something that should be prioritised and subsidised by the government, and whether it truly provides a long-term solution to independent transport.
| Year | E-Bikes sold in the United States (1000s) |
| ------------- | ------------- |
| 2018 | 369 |
| 2019 | 423 |
| 2020 | 416 |
| 2021 | 750 |
| 2022 | 928 |

![data](https://github.com/aahiill/m3-math-modelling-2023/assets/46938400/f3c95217-f9e7-4194-9848-aa4bca261428)

## Assumptions
* The growth in e-bike use will continue at a similar rate to recent years: We assume that the trend of increased e-bike sales and usage will continue for the next five years. While we recognize that external factors may influence the rate of growth, such as changes in consumer preferences or technological advancements, we do not expect any significant disruptions to the trend.
  
* E-bike usage will be influenced by demographic factors: We assume that the age, income, and urbanisation levels of the population will affect the growth of e-bike use. For example, younger, more urban populations with higher incomes may be more likely to adopt e-bikes as a transportation option.

* Public policy will play a role in the growth of e-bike use: We assume that policies aimed at promoting sustainable transportation options, such as tax incentives and investments in bike infrastructure, will influence the growth of e-bike use. However, we also recognize that the impact of these policies may be limited by other factors, such as cultural norms and existing infrastructure.
  
* The growth in e-bike use will be influenced by the availability and cost of alternative transportation options: We assume that the growth of e-bike use will be affected by the availability and cost of other transportation options, such as public transit and personal vehicles. In areas with limited public transit options or high costs of car ownership, e-bikes may be a more attractive alternative.
  
* The growth in e-bike use will be influenced by environmental and health concerns: We assume that increasing awareness of environmental and health issues, such as air pollution and physical activity, will contribute to the growth of e-bike use. As more people become aware of the benefits of sustainable transportation options, they may be more likely to adopt e-bikes as a means of transportation.
  
* E-bikes are an affordable transportation option. Although due to factors such as relative and absolute poverty, in developed countries like the United States, this isn’t a significant enough proportion to invalidate our model, so we can assume that everyone in the United States can afford an E-bike.
  
* E-bikes are motorised bicycles powered with a battery:
  * Electric bikes
  * Mopeds
  * Sit-down scooters
 
## Model Development
Our model considers the gradual increase in e-bikes sold where due to the aforementioned assumptions, a stable trend is expected. The sales of e-bikes in the US, albeit the fall in 2020 acting as an outlier likely due to the effects of COVID-19 on restrictive measures, progressively increases.
Visually looking at the data (Diagram 1), even with the inclusion of 2020, there is a strong positive correlation. As a consequence of this, the most optimal model to use would be a linear regression, as its simplicity reduces the need for time-consuming and cost-inefficient research, and instead predicts future e-bike sales. The time frame is sufficiently short enough that extrapolated data is valid.

From there, we will investigate the percentage error of our model relative to the historical data to prove that it is a valid linear regression model, and can accurately project future sales of e-bikes in the United States.

Creating a second linear regression model is also important, as in the second model, we will omit the data from 2020 as it is anomalous, falling below sales in 2019, and was due to the pandemic rather than consumer demand. While the first linear regression model utilises all data presented to us, we expect the second model to be more accurate; a correlation coefficient value closer to 1 and  less percentage error. This will prove why our second linear regression model, omitting outliers, provides a more valid projection.
The third linear regression model is refined through the use of exponential moving averages, whereby data from the years post-2020 (2021 and 2022) are given greater weight than the data from the years pre-2020 inclusive.

The linear regression model can be mathematically represented below in the form a + bx. I actually took out my calculator and used A-Level stats to get these values.

## Linear Regression Model 1
$$LinearReg_1 = 143.7 + 144.5x$$

$$r = 0.9212 (4dp)$$

Our model considers the gradual increase in e-bikes sold where due to the aforementioned assumptions, a stable trend is expected. The sales of e-bikes in the US, albeit the fall in 2020 acting as an outlier likely due to the effects of COVID-19 on restrictive measures, progressively increases.

| Index | Year | E-Bikes sold in the United States (1000s) | Linear Regression Model | Percentage Error |
| ------------- | ------------- | ------------- | ------------- | ------------- |  
| 1 | 2018 | 369 | 288.2 | (-) 21.90% |
| 2 | 2019 | 423 | 432.7 | (+) 2.29% |
| 3 | 2020 | 416 | 577.2 | (+) 38.75% |
| 4 | 2021 | 750 | 721.7 | (+) 3.92% |
| 5 | 2022 | 928 | 866.2 | (-) 6.66% |
| 8 | 2025 | - | **1299.7** | - | 
| 11 | 2028 | - | **1733.2** | - |

## Linear Regression Model 2
$$LinearReg_2 = 184 + 144.5$$

$$r = 0.9778 (4dp)$$

| Index | Year | E-Bikes sold in the United States (1000s) | Linear Regression Model | Percentage Error |
| ------------- | ------------- | ------------- | ------------- | ------------- |  
| 1 | 2018 | 369 | 329.5 | (-) 10.98% |
| 2 | 2019 | 423 | 473 | (+) 11.82% |
| - | - | - | - | - | 
| 4 | 2021 | 750 | 762 | (+) 1.60% |
| 5 | 2022 | 928 | 906.5 | (-) 2.32% |
| 8 | 2025 | - | **1340** | - | 
| 11 | 2028 | - | **1773** | - |

![linear_reg](https://github.com/aahiill/m3-math-modelling-2023/assets/46938400/837d9745-383e-4db9-aaa8-8ca1684346c3)

Linear regression model 1 excludes index 3 (2020) data point, considering it an anomalous result as it doesn't align with the trend of data. Through removing this index, we achieve a greater correlation coefficient (0.9778 > 0.9212) supporting this choice.

## Linear Regression Model 3
$$LinearReg_3 = LinearReg_2 + 0.1 ~ weighting ~ on ~ 2021 + 0.5 ~ weighting ~ on ~ 2022 $$

| Index | Year | E-Bikes sold in the United States (1000s) | Linear Regression Model | Percentage Error |
| ------------- | ------------- | ------------- | ------------- | ------------- |  
| 1 | 2018 | 369 | 321.1 | (-) 13% |
| 2 | 2019 | 423 | 471.7 | (+) 11.5% |
| - | - | - | - | - | 
| 4 | 2021 | 750 | 772.8 | (+) 3% |
| 5 | 2022 | 928 | 923 | (-) 0.5% |
| 8 | 2025 | - | **1375.1** | - | 
| 11 | 2028 | - | **1826.8** | - |

![weighted_linear_reg](https://github.com/aahiill/m3-math-modelling-2023/assets/46938400/74d85284-d847-441c-a88e-bb8b000a993d)

* Percentage error is small for all years (< ±15%)
* Percentage error for 2021 is very small (< ±3%)
* Percentage error for 2022 is negligible (< ±0.5%)

# Evaluation

## Strengths
A linear regression model is easy to interpret for the average audience, and by extent, the government, who could justify changes in policy using the graphical linear regression models our team has created using Python and Scikit-learn (see graphical representation of models).

Our model is built on iterative developments to refine it and increase its accuracy, allowing it to present us with a greater impression of future projected sales. LinearReg2 uses the fundamentals of LinearReg1, but omits data from index 3 (2020) as it is an outlier, explained in depth in our summary.

Upon cleaning up the data, our correlation coefficient (0.9778) was greater than our previous correlation coefficient (0.9212). This proves that omitting 2020 data leads to a stronger correlation, and justifies our choice of using a linear regression model. Furthermore, it gives us confidence in extrapolating data for later years; 2025 and 2028 projections, if our assumptions are maintained, will only have a slim margin of error at most.

Our model was strengthened through the use of increased weighting of 2021 and 2022 and decreased weighting of 2018 and 2019 with an exponential moving average function. These results compared brilliantly with the data, with a maximum percentage error of 13% as well as increasingly accurate recent data, with 2020 at a 3% error and 2021 at a 0.5% error. Thus, we can expect our extrapolations for 2025 and 2028 to be much closer to the true number of e-bikes sold in the United States.

| Year | E-Bikes sold in the United States (1000s) |
| ------------- | ------------- |
| 2025 | 1375.1 |
| 2028 | 1826.8 |

## Weaknesses

However, our model only uses 5 data points to create the linear regression model, and only considers 4 data points after excluding 2020. Having a limited amount of data, it raises questions about the accuracy of the model for extrapolated data for 2025 and 2028. Although extrapolation for 2025 will be expectedly close to our model, due to its relative short-termness, we can’t be certain that future trends will hold, limiting the validity of extrapolated data for 2028. If smaller intervals were used, this could also provide us with a better representation of the data (for instance, using quartiles instead of years), providing us a better correlation coefficient value. The most prominent weakness of model 3 is the manner in which it was weighted, with weights of 0.05 given to 2018 and 2019, weight of 0.1 for 2021, and a weight of 0.5 for 2022. The weighting was down to judgement and iterative developments of the model, which can bring forth an element of subjectivity to the model.

# Summary

In tackling the question we used 3 linear regression models; through iterative developments we improved our model’s accuracy and validity. The first linear regression model includes all the data. The second linear regression model excludes data from 2020 as it is considered anomalous to the extent it interferes with our predictions. The third linear regression model weights gives precedent to the most recent data points (2021 and 2022) to adjust to consumer demand following the COVID-19 pandemic that ignited the e-bike industry all over the world.

## The Role of COVID-19
Upon investigating the data, we identified the boom in consumer demand for electric bikes following 2020. Therefore we recognised that the decrease in sales in 2020 was unorthodox, and must have been due to external factors. Decreasing prices in lithium ion batteries could be considered, however this should have the opposite effect on demand. 

2020 was a year famous for all the wrong reasons.

COVID-19 restrictive measures were abundant throughout the United States, with people forced to stay at home and restricted access to retail shopping, and to some extent, shopping for daily necessities. This undoubtedly put financial strain on many, which contributed to the lack of e-bikes purchased. Though crucially, the restrictions placed as a consequence of the pandemic meant less people needed transport. Therefore 2020 can only be taken in isolation, as it's an outlier to our standard results, and following 2020, there was incredible growth.

Sales of E-bikes dipped massively right at the start of Covid-19, in March 2020 due to lockdowns as well as supply chains being disrupted and manufacturing facilities being shut down, however these sales skyrocketed later on in the year as the imposed lockdowns were gradually removed and more people were able to go out. People were still social distancing, E-bikes allowed people to stay active while social distancing.

As the data used for the regression models above does not specify which month each value was taken from throughout the year, we acknowledge 2020 as an outlier as during the year there was both a massive decrease and increase in sales and as we cannot identify whether the data was pre or post COVID-19. This increase of sales however, can be seen with the 2021 and 2022 data of the above linear regression models, dramatically increased.

## Linear Regression Model Weighting
* We put less weight in years pre-2020 (2018, 2019) as they don’t account for the newfound consumer preference and market trend in the United States

* We put more weight in years post-2020 (2021, 2022) as it accounts for the newfound consumer preference and market trends in the United States

* E-bikes are the largest segment by battery type (as in majority of lithium ion batteries go into battery-powered vehicles like e-bikes). Prices of batteries have been falling sharply over the last 10 years, at a rate of ~20% annually. The fall is expected to continue at a rate of around 10% annually over the next five years. The decline in battery prices is expected to increase the demand further during the forecast period. Hence 2022 has the highest weighted average. 
