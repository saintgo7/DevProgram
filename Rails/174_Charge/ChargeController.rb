class ChargeController < ApplicationController
  before_action :set_charge, only: [:show, :edit, :update, :destroy]

  # GET /charge
  def index
    @charges = Charge.all
    render json: @charges
  end

  # GET /charge/1
  def show
    render json: @charge
  end

  # POST /charge
  def create
    @charge = Charge.new(charge_params)

    if @charge.save
      render json: @charge, status: :created
    else
      render json: @charge.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /charge/1
  def update
    if @charge.update(charge_params)
      render json: @charge
    else
      render json: @charge.errors, status: :unprocessable_entity
    end
  end

  # DELETE /charge/1
  def destroy
    @charge.destroy
    head :no_content
  end

  private

  def set_charge
    @charge = Charge.find(params[:id])
  end

  def charge_params
    params.require(:charge).permit(:name)
  end
end
