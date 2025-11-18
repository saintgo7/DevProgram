class StockController < ApplicationController
  before_action :set_stock, only: [:show, :edit, :update, :destroy]

  # GET /stock
  def index
    @stocks = Stock.all
    render json: @stocks
  end

  # GET /stock/1
  def show
    render json: @stock
  end

  # POST /stock
  def create
    @stock = Stock.new(stock_params)

    if @stock.save
      render json: @stock, status: :created
    else
      render json: @stock.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /stock/1
  def update
    if @stock.update(stock_params)
      render json: @stock
    else
      render json: @stock.errors, status: :unprocessable_entity
    end
  end

  # DELETE /stock/1
  def destroy
    @stock.destroy
    head :no_content
  end

  private

  def set_stock
    @stock = Stock.find(params[:id])
  end

  def stock_params
    params.require(:stock).permit(:name)
  end
end
