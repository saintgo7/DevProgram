class CustomsController < ApplicationController
  before_action :set_customs, only: [:show, :edit, :update, :destroy]

  # GET /customs
  def index
    @customss = Customs.all
    render json: @customss
  end

  # GET /customs/1
  def show
    render json: @customs
  end

  # POST /customs
  def create
    @customs = Customs.new(customs_params)

    if @customs.save
      render json: @customs, status: :created
    else
      render json: @customs.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /customs/1
  def update
    if @customs.update(customs_params)
      render json: @customs
    else
      render json: @customs.errors, status: :unprocessable_entity
    end
  end

  # DELETE /customs/1
  def destroy
    @customs.destroy
    head :no_content
  end

  private

  def set_customs
    @customs = Customs.find(params[:id])
  end

  def customs_params
    params.require(:customs).permit(:name)
  end
end
