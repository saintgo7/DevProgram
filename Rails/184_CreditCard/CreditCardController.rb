class CreditCardController < ApplicationController
  before_action :set_creditcard, only: [:show, :edit, :update, :destroy]

  # GET /creditcard
  def index
    @creditcards = CreditCard.all
    render json: @creditcards
  end

  # GET /creditcard/1
  def show
    render json: @creditcard
  end

  # POST /creditcard
  def create
    @creditcard = CreditCard.new(creditcard_params)

    if @creditcard.save
      render json: @creditcard, status: :created
    else
      render json: @creditcard.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /creditcard/1
  def update
    if @creditcard.update(creditcard_params)
      render json: @creditcard
    else
      render json: @creditcard.errors, status: :unprocessable_entity
    end
  end

  # DELETE /creditcard/1
  def destroy
    @creditcard.destroy
    head :no_content
  end

  private

  def set_creditcard
    @creditcard = CreditCard.find(params[:id])
  end

  def creditcard_params
    params.require(:creditcard).permit(:name)
  end
end
