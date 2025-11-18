class ChartController < ApplicationController
  before_action :set_chart, only: [:show, :edit, :update, :destroy]

  # GET /chart
  def index
    @charts = Chart.all
    render json: @charts
  end

  # GET /chart/1
  def show
    render json: @chart
  end

  # POST /chart
  def create
    @chart = Chart.new(chart_params)

    if @chart.save
      render json: @chart, status: :created
    else
      render json: @chart.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /chart/1
  def update
    if @chart.update(chart_params)
      render json: @chart
    else
      render json: @chart.errors, status: :unprocessable_entity
    end
  end

  # DELETE /chart/1
  def destroy
    @chart.destroy
    head :no_content
  end

  private

  def set_chart
    @chart = Chart.find(params[:id])
  end

  def chart_params
    params.require(:chart).permit(:name)
  end
end
