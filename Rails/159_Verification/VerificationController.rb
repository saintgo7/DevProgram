class VerificationController < ApplicationController
  before_action :set_verification, only: [:show, :edit, :update, :destroy]

  # GET /verification
  def index
    @verifications = Verification.all
    render json: @verifications
  end

  # GET /verification/1
  def show
    render json: @verification
  end

  # POST /verification
  def create
    @verification = Verification.new(verification_params)

    if @verification.save
      render json: @verification, status: :created
    else
      render json: @verification.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /verification/1
  def update
    if @verification.update(verification_params)
      render json: @verification
    else
      render json: @verification.errors, status: :unprocessable_entity
    end
  end

  # DELETE /verification/1
  def destroy
    @verification.destroy
    head :no_content
  end

  private

  def set_verification
    @verification = Verification.find(params[:id])
  end

  def verification_params
    params.require(:verification).permit(:name)
  end
end
