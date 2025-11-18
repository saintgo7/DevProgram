class AccountController < ApplicationController
  before_action :set_account, only: [:show, :edit, :update, :destroy]

  # GET /account
  def index
    @accounts = Account.all
    render json: @accounts
  end

  # GET /account/1
  def show
    render json: @account
  end

  # POST /account
  def create
    @account = Account.new(account_params)

    if @account.save
      render json: @account, status: :created
    else
      render json: @account.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /account/1
  def update
    if @account.update(account_params)
      render json: @account
    else
      render json: @account.errors, status: :unprocessable_entity
    end
  end

  # DELETE /account/1
  def destroy
    @account.destroy
    head :no_content
  end

  private

  def set_account
    @account = Account.find(params[:id])
  end

  def account_params
    params.require(:account).permit(:name)
  end
end
