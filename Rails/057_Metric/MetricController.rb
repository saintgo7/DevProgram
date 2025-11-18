class MetricController < ApplicationController
  before_action :set_metric, only: [:show, :edit, :update, :destroy]

  # GET /metric
  def index
    @metrics = Metric.all
    render json: @metrics
  end

  # GET /metric/1
  def show
    render json: @metric
  end

  # POST /metric
  def create
    @metric = Metric.new(metric_params)

    if @metric.save
      render json: @metric, status: :created
    else
      render json: @metric.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /metric/1
  def update
    if @metric.update(metric_params)
      render json: @metric
    else
      render json: @metric.errors, status: :unprocessable_entity
    end
  end

  # DELETE /metric/1
  def destroy
    @metric.destroy
    head :no_content
  end

  private

  def set_metric
    @metric = Metric.find(params[:id])
  end

  def metric_params
    params.require(:metric).permit(:name)
  end
end
