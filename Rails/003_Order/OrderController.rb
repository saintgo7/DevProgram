class OrderController < ApplicationController
  before_action :set_order, only: [:show, :edit, :update, :destroy]

  # GET /order
  def index
    @orders = Order.all
    render json: @orders
  end

  # GET /order/1
  def show
    render json: @order
  end

  # POST /order
  def create
    @order = Order.new(order_params)

    if @order.save
      render json: @order, status: :created
    else
      render json: @order.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /order/1
  def update
    if @order.update(order_params)
      render json: @order
    else
      render json: @order.errors, status: :unprocessable_entity
    end
  end

  # DELETE /order/1
  def destroy
    @order.destroy
    head :no_content
  end

  private

  def set_order
    @order = Order.find(params[:id])
  end

  def order_params
    params.require(:order).permit(:name)
  end
end
