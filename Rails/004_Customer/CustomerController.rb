class CustomerController < ApplicationController
  before_action :set_customer, only: [:show, :edit, :update, :destroy]

  # GET /customer
  def index
    @customers = Customer.all
    render json: @customers
  end

  # GET /customer/1
  def show
    render json: @customer
  end

  # POST /customer
  def create
    @customer = Customer.new(customer_params)

    if @customer.save
      render json: @customer, status: :created
    else
      render json: @customer.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /customer/1
  def update
    if @customer.update(customer_params)
      render json: @customer
    else
      render json: @customer.errors, status: :unprocessable_entity
    end
  end

  # DELETE /customer/1
  def destroy
    @customer.destroy
    head :no_content
  end

  private

  def set_customer
    @customer = Customer.find(params[:id])
  end

  def customer_params
    params.require(:customer).permit(:name)
  end
end
