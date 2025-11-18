class EncryptionController < ApplicationController
  before_action :set_encryption, only: [:show, :edit, :update, :destroy]

  # GET /encryption
  def index
    @encryptions = Encryption.all
    render json: @encryptions
  end

  # GET /encryption/1
  def show
    render json: @encryption
  end

  # POST /encryption
  def create
    @encryption = Encryption.new(encryption_params)

    if @encryption.save
      render json: @encryption, status: :created
    else
      render json: @encryption.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /encryption/1
  def update
    if @encryption.update(encryption_params)
      render json: @encryption
    else
      render json: @encryption.errors, status: :unprocessable_entity
    end
  end

  # DELETE /encryption/1
  def destroy
    @encryption.destroy
    head :no_content
  end

  private

  def set_encryption
    @encryption = Encryption.find(params[:id])
  end

  def encryption_params
    params.require(:encryption).permit(:name)
  end
end
