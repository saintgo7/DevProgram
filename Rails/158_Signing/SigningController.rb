class SigningController < ApplicationController
  before_action :set_signing, only: [:show, :edit, :update, :destroy]

  # GET /signing
  def index
    @signings = Signing.all
    render json: @signings
  end

  # GET /signing/1
  def show
    render json: @signing
  end

  # POST /signing
  def create
    @signing = Signing.new(signing_params)

    if @signing.save
      render json: @signing, status: :created
    else
      render json: @signing.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /signing/1
  def update
    if @signing.update(signing_params)
      render json: @signing
    else
      render json: @signing.errors, status: :unprocessable_entity
    end
  end

  # DELETE /signing/1
  def destroy
    @signing.destroy
    head :no_content
  end

  private

  def set_signing
    @signing = Signing.find(params[:id])
  end

  def signing_params
    params.require(:signing).permit(:name)
  end
end
