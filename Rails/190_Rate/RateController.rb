class RateController < ApplicationController
  before_action :set_rate, only: [:show, :edit, :update, :destroy]

  # GET /rate
  def index
    @rates = Rate.all
    render json: @rates
  end

  # GET /rate/1
  def show
    render json: @rate
  end

  # POST /rate
  def create
    @rate = Rate.new(rate_params)

    if @rate.save
      render json: @rate, status: :created
    else
      render json: @rate.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /rate/1
  def update
    if @rate.update(rate_params)
      render json: @rate
    else
      render json: @rate.errors, status: :unprocessable_entity
    end
  end

  # DELETE /rate/1
  def destroy
    @rate.destroy
    head :no_content
  end

  private

  def set_rate
    @rate = Rate.find(params[:id])
  end

  def rate_params
    params.require(:rate).permit(:name)
  end
end
