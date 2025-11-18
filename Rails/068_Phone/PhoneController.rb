class PhoneController < ApplicationController
  before_action :set_phone, only: [:show, :edit, :update, :destroy]

  # GET /phone
  def index
    @phones = Phone.all
    render json: @phones
  end

  # GET /phone/1
  def show
    render json: @phone
  end

  # POST /phone
  def create
    @phone = Phone.new(phone_params)

    if @phone.save
      render json: @phone, status: :created
    else
      render json: @phone.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /phone/1
  def update
    if @phone.update(phone_params)
      render json: @phone
    else
      render json: @phone.errors, status: :unprocessable_entity
    end
  end

  # DELETE /phone/1
  def destroy
    @phone.destroy
    head :no_content
  end

  private

  def set_phone
    @phone = Phone.find(params[:id])
  end

  def phone_params
    params.require(:phone).permit(:name)
  end
end
